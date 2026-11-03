---
title: "Safely Updating Hermes When Hermes Runs in Docker"
date: 2026-11-03T12:00:00+01:00
url: /2026/11/safely-updating-hermes-when-hermes-runs-in-docker/
author: Thomas Faddegon
categories:
  - linux
  - programmeren
  - security
tags:
  - howto
  - docker
  - hermes
  - systemd
cover:
  image: cover.jpg
  alt: A small robot hands an update package to a host control panel while generic server containers, a shield and rollback arrows show a safe upgrade
---
**The Problem**

I run [Hermes](https://hermes-agent.nousresearch.com/) as a Docker container. Asking it to pull its own new image is easy. Letting that same container recreate itself is where things get interesting.

A normal update looks harmless:

```bash
docker compose pull hermes
docker compose up -d --force-recreate hermes
```

But when Hermes runs those commands from inside itself, `docker compose up` removes the container that is currently executing the update. The SSH session, shell or agent call can disappear after the old container is removed but before the replacement is started. The result is a Hermes container stuck in `Created`, and nobody left to finish the command.

The fix is not another retry inside Hermes. The update must be owned by something that survives Hermes being replaced.

**The Design**

I use the host user's systemd manager as supervisor:

```text
Hermes → host launcher → systemd user service → update script
                                      ↓
                         pull, backup, recreate,
                         health check or rollback
```

Hermes only launches the unit. The host-side unit keeps running when the Hermes container disappears.

This setup also avoids mounting the Docker socket into Hermes. If Hermes already has a secure way to execute a command on its host, such as a restricted SSH key, it can call the launcher through that route. Otherwise I start the systemd unit manually on the host.

The examples below assume:

- Linux with Docker Compose v2;
- a Compose project in `/srv/hermes`;
- the Compose service and container are both named `hermes`;
- persistent Hermes state lives in `/srv/hermes/data`;
- the host user can run Docker without `sudo`.

Change those values before installing it. Do not blindly copy paths from somebody else's server.

**1. The Host-Side Update Script**

Save this as `/srv/hermes/hermes-safe-update.sh`:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

BASE=${HERMES_BASE:-/srv/hermes}
SERVICE=${HERMES_SERVICE:-hermes}
IMAGE=${HERMES_IMAGE:-nousresearch/hermes-agent:latest}
HEALTH_URL=${HERMES_HEALTH_URL:-}
HEALTH_TIMEOUT=${HERMES_HEALTH_TIMEOUT:-240}
STABLE_SECONDS=${HERMES_STABLE_SECONDS:-20}
BACKUP_ROOT="$BASE/update-backups"
LOG_ROOT="$BASE/update-logs"
LOCK="$BASE/.hermes-update.lock"
MODE=${1:-run}

mkdir -p "$BACKUP_ROOT" "$LOG_ROOT"
exec 9>"$LOCK"
flock -n 9 || { echo "ERROR: another Hermes update is already running"; exit 75; }

stamp=$(date -u +%Y%m%dT%H%M%SZ)
log="$LOG_ROOT/$stamp.log"
exec > >(tee -a "$log") 2>&1

logmsg() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*"; }
container_image() { docker inspect --format '{{.Image}}' "$SERVICE"; }
local_image() { docker image inspect "$IMAGE" --format '{{.Id}}'; }
container_running() {
  [ "$(docker inspect --format '{{.State.Running}}' "$SERVICE" 2>/dev/null || true)" = true ]
}

health_once() {
  container_running || return 1
  docker exec "$SERVICE" hermes gateway status >/dev/null 2>&1 || return 1
  [ -z "$HEALTH_URL" ] || {
    code=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 5 "$HEALTH_URL" || true)
    case "$code" in 2??|3??|401|403) ;; *) return 1 ;; esac
  }
}

wait_healthy() {
  local deadline=$((SECONDS + HEALTH_TIMEOUT))
  while (( SECONDS < deadline )); do
    if health_once; then
      logmsg "Initial health check passed; checking stability for ${STABLE_SECONDS}s"
      sleep "$STABLE_SECONDS"
      health_once && return 0
    fi
    sleep 5
  done
  return 1
}

backup_state() {
  local dest=$1
  mkdir -p "$dest"
  cp -a --reflink=auto "$BASE/data" "$dest/data"
  cp -a "$BASE/compose.yaml" "$dest/compose.yaml"
  printf '%s\n' "$old_id" > "$dest/old-image-id"
  printf '%s\n' "$new_id" > "$dest/new-image-id"
}

restore_state() {
  local src=$1
  rm -rf "$BASE/data"
  cp -a --reflink=auto "$src/data" "$BASE/data"
}

cd "$BASE"
docker compose config -q
old_id=$(container_image)
logmsg "Current container image: $old_id"

if [ "$MODE" = check ]; then
  health_once
  logmsg "CHECK_OK compose valid, current gateway healthy"
  exit 0
fi
[ "$MODE" = run ] || { echo "Usage: $0 [check|run]"; exit 64; }

logmsg "Pulling latest image for $SERVICE"
docker compose pull "$SERVICE"
new_id=$(local_image)
logmsg "Pulled latest image: $new_id"

if [ "$old_id" = "$new_id" ]; then
  logmsg "NO_UPDATE image already current"
  exit 0
fi

backup="$BACKUP_ROOT/$stamp"
rollback_tag="hermes-agent-rollback:$stamp"
docker image tag "$old_id" "$rollback_tag"
logmsg "Rollback image tagged as $rollback_tag"

logmsg "Stopping Hermes for a consistent state backup"
docker compose stop "$SERVICE"
backup_state "$backup"
logmsg "State backup completed: $backup"

logmsg "Starting new image"
if docker compose up -d --no-deps --force-recreate "$SERVICE" && wait_healthy; then
  actual=$(container_image)
  if [ "$actual" = "$new_id" ]; then
    logmsg "UPDATE_OK old=$old_id new=$new_id backup=$backup"
    exit 0
  fi
  logmsg "ERROR running image $actual does not equal expected $new_id"
fi

logmsg "UPDATE_FAILED; starting automatic rollback"
docker compose stop "$SERVICE" || true
restore_state "$backup"
docker image tag "$old_id" "$IMAGE"
docker compose up -d --no-deps --force-recreate "$SERVICE"

if wait_healthy && [ "$(container_image)" = "$old_id" ]; then
  logmsg "ROLLBACK_OK restored=$old_id backup=$backup"
  exit 20
fi

logmsg "ROLLBACK_FAILED manual intervention required; backup=$backup old_image=$old_id"
docker compose ps "$SERVICE" || true
docker logs --tail 200 "$SERVICE" || true
exit 21
```

Make it executable and test the read-only check first:

```bash
chmod 700 /srv/hermes/hermes-safe-update.sh
/srv/hermes/hermes-safe-update.sh check
```

The script deliberately stops Hermes before copying its data. Hermes uses SQLite databases, and copying a live database without its current WAL files is a good way to discover that a backup was never really a backup.

It also copies the entire persistent data directory. That costs more disk space than selecting a few files, but it is much harder to forget a newly added database, profile or plugin.

**2. Let systemd Own the Update**

Create `~/.config/systemd/user/hermes-safe-update.service` on the Docker host:

```ini
[Unit]
Description=Host-supervised safe Hermes update
After=docker.service

[Service]
Type=oneshot
WorkingDirectory=/srv/hermes
ExecStart=/srv/hermes/hermes-safe-update.sh run
TimeoutStartSec=15min
```

Then load it:

```bash
systemctl --user daemon-reload
systemctl --user enable-linger "$USER"
systemctl --user start hermes-safe-update.service
journalctl --user -fu hermes-safe-update.service
```

`enable-linger` lets the user's systemd manager keep running without an interactive login. That is important when an unattended update temporarily removes the very container that requested it.

**3. Use a Tiny Launcher**

Save this as `/srv/hermes/launch-hermes-safe-update.sh`:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

unit=hermes-safe-update.service
if systemctl --user is-active --quiet "$unit"; then
  echo "ALREADY_RUNNING unit=$unit"
  exit 75
fi

systemctl --user reset-failed "$unit" >/dev/null 2>&1 || true
systemctl --user start --no-block "$unit"
echo "UPDATE_LAUNCHED unit=$unit"
echo "Follow on host: journalctl --user -fu $unit"
```

And lock down its permissions:

```bash
chmod 700 /srv/hermes/launch-hermes-safe-update.sh
```

Hermes can now ask the host to run only the launcher. For example, over an existing restricted SSH route:

```bash
ssh update-host /srv/hermes/launch-hermes-safe-update.sh
```

Do not give an AI container unrestricted host access just to solve updates. Prefer a dedicated SSH key with a forced command, or start the systemd unit yourself. Also do not expose a Docker TCP API: control of Docker is effectively root access to the host.

**What Happens During an Update**

The sequence is intentionally boring:

1. Validate the Compose file and acquire a lock.
2. Record the image currently used by the running container.
3. Pull the configured image.
4. Exit without downtime when the image ID did not change.
5. Tag the old image so pruning cannot remove the rollback target.
6. Stop Hermes and make a consistent state backup.
7. Recreate only the Hermes service, not sibling containers.
8. Check `hermes gateway status`, wait briefly and check again.
9. Restore the old state and image automatically if the new container is unhealthy.

The `--no-deps` flag matters when the Compose project contains other services. Updating Hermes should not restart a database, synchronization service or anything else that happened to share the file.

**Useful Checks**

Before trusting the automation, run:

```bash
# Validate configuration and current health
/srv/hermes/hermes-safe-update.sh check

# Start an update through the durable supervisor
systemctl --user start hermes-safe-update.service

# Follow progress
journalctl --user -fu hermes-safe-update.service

# Inspect recent file logs
ls -lt /srv/hermes/update-logs/

# Confirm which image the container actually runs
docker inspect --format '{{.Image}}' hermes
```

If Hermes exposes a local dashboard or gateway endpoint, set an additional health URL in the unit:

```ini
Environment=HERMES_HEALTH_URL=http://127.0.0.1:PORT/
```

The script accepts `2xx`, `3xx`, `401` and `403` there. A protected endpoint can be healthy without returning a public `200`.

**The Fine Print**

- The example expects GNU `cp` for `--reflink=auto`. On a filesystem without reflinks it performs a normal copy.
- Backups can contain credentials. Keep `/srv/hermes` private and add retention or encrypted off-host backups if you need disaster recovery.
- This protects the application update, not the host itself. A disk failure can still take the container and local backups together.
- A floating `latest` tag is convenient, but the image-ID comparison is what determines whether anything actually changed.
- Run a real failure test once: temporarily configure an invalid health URL, confirm rollback, then remove it. An untested rollback is just optimistic documentation.

**Three Takeaways**

1. A container should not be responsible for completing its own replacement.
2. Hand the update to a host-side supervisor, then verify health after the new container starts.
3. Back up persistent state and retain the old image before recreating anything.

*Full disclosure: Hermes helped design, test and document this update procedure—including the rule that prevents it from cutting off its own update halfway through.*

Happy updating!