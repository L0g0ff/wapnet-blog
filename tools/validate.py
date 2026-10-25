#!/usr/bin/env python3
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
SITE_HOST = "blog.wapnet.nl"
# ponytail: preserve known source 404s; remove these exceptions if the files are recovered.
KNOWN_SOURCE_404S = {
    "/upload/HTCS710-MonaLisa-61.zip",
    "/upload/65officialv10.exe",
    "/upload/65v11.exe",
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        del tag
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.urls.append(value)
            elif name == "srcset" and value:
                self.urls.extend(part.strip().split()[0] for part in value.split(","))


def output_path(url):
    parsed = urlsplit(url)
    if parsed.netloc and parsed.hostname != SITE_HOST:
        return None
    path = unquote(parsed.path)
    if not path or path == "/":
        return PUBLIC / "index.html"
    candidate = PUBLIC / path.lstrip("/")
    if path.endswith("/"):
        return candidate / "index.html"
    if candidate.suffix:
        return candidate
    return candidate if candidate.exists() else candidate / "index.html"


def main():
    inventory = json.loads((ROOT / "inventory/source.json").read_text(encoding="utf-8"))
    source_urls = [item["link"] for kind in ("posts", "pages") for item in inventory[kind]]
    missing_pages = []
    for url in source_urls:
        target = output_path(url)
        if target is None or not target.is_file():
            missing_pages.append(url)
    assert len(source_urls) == 326
    assert not missing_pages, missing_pages[:10]

    upload_files = [path for path in (ROOT / "static/wp-content/uploads").rglob("*") if path.is_file()]
    legacy_files = [path for path in (ROOT / "static/upload").rglob("*") if path.is_file()]
    assert len(upload_files) == 1379, len(upload_files)
    assert len(legacy_files) == 5, len(legacy_files)

    required = ["index.html", "about/index.html", "feed.xml", "sitemap.xml", "404.html"]
    assert all((PUBLIC / path).is_file() for path in required)

    html_files = list(PUBLIC.rglob("*.html"))
    broken_assets = set()
    for html_file in html_files:
        parser = Links()
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        for url in parser.urls:
            target = output_path(url)
            if target is None or url.startswith(("mailto:", "tel:", "javascript:")):
                continue
            path = urlsplit(url).path
            if path.startswith(("/wp-content/", "/upload/", "/assets/")) and not target.is_file():
                broken_assets.add((html_file.relative_to(PUBLIC).as_posix(), url))
    unexpected_broken = {(page, url) for page, url in broken_assets if urlsplit(url).path not in KNOWN_SOURCE_404S}
    assert not unexpected_broken, sorted(unexpected_broken)[:20]

    content = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "content").rglob("*.md"))
    assert not re.search(r"\\\[(?:code|paypal-donation)(?:[^]]*)\\\]", content, re.I)
    homepage = (PUBLIC / "index.html").read_text(encoding="utf-8")
    assert "Wapnet Blog" in homepage
    assert "MIFARE Classic on Flipper Zero" in homepage
    assert "example.org" not in homepage

    print(
        f"source_urls={len(source_urls)} html_pages={len(html_files)} "
        f"uploads={len(upload_files)} legacy_downloads={len(legacy_files)} "
        f"known_source_404s={len({urlsplit(url).path for _, url in broken_assets})} "
        "unexpected_broken_assets=0"
    )


if __name__ == "__main__":
    main()
