#!/usr/bin/env python3
import json
import urllib.request
from pathlib import Path

BASE = "https://blog.wapnet.nl/wp-json/wp/v2"
FIELDS = "id,date,modified,link,slug,status,type,title,categories,tags,featured_media,comment_status"


def fetch_all(endpoint, fields=None):
    items = []
    page = 1
    while True:
        query = f"per_page=100&page={page}&orderby=id&order=asc"
        if fields:
            query += f"&_fields={fields}"
        request = urllib.request.Request(
            f"{BASE}/{endpoint}?{query}", headers={"User-Agent": "wapnet-hugo-inventory/1"}
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            items.extend(json.load(response))
            pages = int(response.headers.get("X-WP-TotalPages", "1"))
        if page >= pages:
            return items
        page += 1


def main():
    posts = fetch_all("posts", FIELDS)
    pages = fetch_all("pages", FIELDS)
    media = fetch_all("media", "id,date,modified,link,slug,source_url,media_type,mime_type")
    categories = fetch_all("categories", "id,name,slug,count,parent")
    tags = fetch_all("tags", "id,name,slug,count")
    assert len(posts) == 325
    assert len(pages) == 1
    assert len(media) in {399, 400}  # REST omits one of 400 WP attachment records.
    inventory = {
        "summary": {
            "published_posts": len(posts),
            "published_pages": len(pages),
            "public_media": len(media),
            "wordpress_attachment_records": 400,
        },
        "posts": posts,
        "pages": pages,
        "media": media,
        "categories": categories,
        "tags": tags,
    }
    Path("inventory/source.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    Path("inventory/urls.txt").write_text(
        "".join(sorted(item["link"] + "\n" for kind in ("posts", "pages") for item in inventory[kind])),
        encoding="utf-8",
    )
    print(
        f"posts={len(inventory['posts'])} pages={len(inventory['pages'])} "
        f"media={len(inventory['media'])} categories={len(inventory['categories'])} "
        f"tags={len(inventory['tags'])}"
    )


if __name__ == "__main__":
    main()
