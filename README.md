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

## Going live

The workflow currently builds with `HUGO_ENVIRONMENT: staging`, which adds `noindex` so the Pages copy does not compete with the live WordPress site. At cutover:

1. Add `static/CNAME` containing `blog.wapnet.nl` and set the custom domain in **Settings → Pages**.
2. Change `HUGO_ENVIRONMENT` to `production` and drop the `HUGO_CANONIFYURLS` line in `.github/workflows/publish.yml`.
3. Point the `blog.wapnet.nl` DNS record at GitHub Pages.
