#!/usr/bin/env python3
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

CODE = re.compile(r"\\\[code(?:\s+([^]]*))?\\\](.*?)\\\[/code\\\]", re.I | re.S)
PAYPAL = re.compile(r"\\\[paypal-donation\\\]", re.I)
ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>])")


def convert_code(match):
    attrs, body = match.groups()
    language = ""
    if attrs:
        found = re.search(r'(?:lang|language)=["\']?([\w+-]+)', attrs, re.I)
        if found:
            language = found.group(1).lower()
    body = ESCAPE.sub(r"\1", body.strip())
    return f"\n```{language}\n{body}\n```\n"


def main():
    code_count = paypal_count = 0
    inventory = json.loads(Path("inventory/source.json").read_text(encoding="utf-8"))
    urls = {
        str(item["id"]): urlsplit(item["link"]).path
        for kind in ("posts", "pages")
        for item in inventory[kind]
    }
    seen_ids = set()
    for path in Path("content").rglob("*.md"):
        original = path.read_text(encoding="utf-8")
        updated, codes = CODE.subn(convert_code, original)
        updated, paypals = PAYPAL.subn("{{< paypal-donation >}}", updated)
        post_id = re.search(r'^post_id: ["\']?(\d+)["\']?$', updated, re.M)
        if post_id:
            if post_id.group(1) in urls:
                seen_ids.add(post_id.group(1))
                expected = f"url: {urls[post_id.group(1)]}"
                updated = re.sub(r"^url: .*$", expected, updated, count=1, flags=re.M)
                updated = re.sub(r'^draft: ["\']?true["\']?\n', "", updated, count=1, flags=re.M | re.I)
            else:
                updated, marked = re.subn(r"^draft: .*$", "draft: true", updated, count=1, flags=re.M)
                if not marked:
                    updated = updated.replace("---\n", "---\ndraft: true\n", 1)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
        code_count += codes
        paypal_count += paypals
    remaining_code = remaining_paypal = 0
    for path in Path("content").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        remaining_code += len(CODE.findall(text))
        remaining_paypal += len(PAYPAL.findall(text))
    assert remaining_code == 0
    assert remaining_paypal == 0
    assert seen_ids == set(urls), sorted(set(urls) - seen_ids)[:10]
    print(
        f"converted_code_blocks={code_count} converted_paypal_shortcodes={paypal_count} "
        f"verified_public_urls={len(seen_ids)}"
    )


if __name__ == "__main__":
    main()
