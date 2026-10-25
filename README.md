# Wapnet Blog

Hugo source for [blog.wapnet.nl](https://blog.wapnet.nl), migrated from WordPress.

## Writing a post

Add a Markdown file under `content/posts/YYYY/MM/`:

```markdown
---
title: My new post
date: 2026-10-25T12:00:00+02:00
url: /2026/10/my-new-post/
categories: [linux]
tags: [howto]
---
Post body in Markdown.
```

Keep the `url:` in `/:year/:month/:slug/` form so it matches the existing permalinks. Push to `main` and the **Publish** workflow builds and deploys to GitHub Pages.

## Local build

```sh
hugo server                       # live preview on http://localhost:1313
hugo --minify --gc && python3 tools/validate.py
```

`tools/validate.py` fails the build if any original WordPress URL, upload, or legacy download goes missing.

## Hosting

Served by GitHub Pages on the custom domain `blog.wapnet.nl` (`static/CNAME`). DNS lives in Cloudflare: `blog` is a `CNAME` to `l0g0ff.github.io`.

Rollback: point `blog` back at the old WordPress host `185.104.29.138` (A record). The WordPress install at ZXCS is kept frozen as a fallback.
