---
title: "From WordPress to Hugo: Why My Blog Is Now 100% Static"
date: 2026-10-25T07:00:00+01:00
url: /2026/10/from-wordpress-to-hugo-after-a-php-scare/
author: Thomas Faddegon
categories:
  - wordpress
  - linux
tags:
  - hugo
  - github
  - security
cover:
  image: cover.jpg
  alt: A stressed server tangled in PHP cables hands over to a happy robot carrying a clean static web page into the cloud
---
**The Wake-Up Call**

A few days ago my hosting provider sent me a friendly message: *"Warning: 500 emails have just been sent by your account."* Not what you want to read on a Saturday evening.

My first thought: someone dropped a PHP shell on my WordPress blog and is using it as a spam cannon. I renamed PHPMailer as an emergency brake and started digging.

**What It Actually Was**

The good news: no shell. WordPress core and all plugins passed their checksum checks, and there were no unknown admin logins. The culprit was my own security plugin. Wordfence was blocking a brute-force wave of about 500 login attempts, and it was configured to send me an email for *every single block*, with no hourly limit. So the security plugin did its job and still got me an abuse warning.

I fixed the alert settings and disabled outgoing WordPress mail entirely. Problem solved... for now.

**The Real Problem**

That evening made something painfully clear. To publish a handful of tech posts per year, I was running:

- PHP and a MySQL database
- WordPress core plus 8 plugins, all needing updates
- A security plugin to protect all of the above
- A login page that the whole internet keeps hammering

That's a lot of attack surface for what is basically a collection of text files with some screenshots. My blog doesn't *need* to execute anything. So I decided: **static only**. No PHP, no database, no login page. Just HTML.

**The Plan**

- Generator: [Hugo](https://gohugo.io/), a fast, single binary, Markdown in, HTML out
- Importer: [wp2hugo](https://github.com/ashishb/wp2hugo), which turns a WordPress XML export into a Hugo site, media included
- Hosting: GitHub Pages, deployed by a GitHub Action on every push

The one hard requirement: **every existing URL must keep working**. 18 years of posts are indexed and linked all over the internet, so `/2012/04/some-post/` has to stay exactly `/2012/04/some-post/`.

**Step 1: Back Up Everything**

Before touching anything, I pulled a full backup over SSH with WP-CLI and tar:

```bash
wp db export - | gzip > database.sql.gz
wp export --stdout --max_file_size=-1 | gzip > wordpress.xml.gz
tar -czf - wp-content/uploads > uploads.tar.gz
```

Then I verified it with checksums and counts: 325 posts, 1 page, 1,379 upload files (88 MB). Production stayed untouched during the whole migration.

**Step 2: Import with wp2hugo**

```bash
wp2hugo --source wordpress.xml --output import-output \
  --download-media --download-all \
  --content-date-folder-structure year-month
```

A few minutes later I had a working Hugo site with posts, categories, tags, featured images and the PaperMod theme. Impressive, but not perfect.

**Step 3: Fix the Leftovers (Repeatably)**

WordPress sites collect weird stuff over the years. Mine had:

- **Dozens of `[code]` shortcodes** from the old SyntaxHighlighter plugin. They came through as escaped text instead of code blocks.
- **A PayPal donation plugin** whose form had stopped working anyway.
- **Some wrong URLs** where the importer used `/` as the permalink.

Instead of hand-editing 325 files, I wrote one small Python script, `normalize.py`, that converts the `[code]` shortcodes to proper Markdown code fences and resets every post's URL from the original WordPress inventory. If I need to re-import, I just run it again.

**Step 4: Trust, but Verify**

A migration you can't verify is a migration you can't trust. A second script, `validate.py`, fails the build when:

- any of the 326 original post/page URLs is missing
- any upload or legacy download disappears
- an unconverted `[code]` shortcode sneaks back in

That check runs in the GitHub Action on every push, so I can't accidentally break old links later.

**Step 5: Make It Look Like Home**

My old blog had a fixed background photo behind a semi-transparent content area. I kept that idea with a new tech-desk background, kept Disqus so all the old comments still show up, and turned the broken PayPal form into a simple, bright yellow PayPal.me button.

**Step 6: Publish with GitHub Actions**

The workflow is short: install Hugo, build, validate, upload to GitHub Pages. Writing a new post is now just a Markdown file in `content/posts/` and:

```bash
git add . && git commit -m "New post" && git push
```

Push, wait a minute, done. No admin panel, no plugin updates, no PHP.

**The Result**

- 325 posts and all media migrated, with every old URL intact
- Categories, tags, RSS feed, sitemap and comments preserved
- Zero server-side code to patch or exploit
- Free hosting, and the whole blog lives in a Git repository

**Three Takeaways**

1. A security plugin can become the problem. Always set an alert rate limit.
2. If your content doesn't need a server, don't run one. Every plugin is attack surface.
3. Automate the migration fixes and validate everything. Re-running a script beats fixing 325 files by hand.

*Full disclosure: I did this migration together with my AI assistant, which handled most of the tedious backup, import and validation work while I made the decisions. Fitting for a tech blog, I think.* 😉

Happy static blogging!
