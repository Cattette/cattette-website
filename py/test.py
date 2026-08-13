
#!/usr/bin/env python3
"""
Convert a single Bible XML file into one Hugo Markdown file per book.

Written for the common "Zefania XML" Bible format, which looks like:

<XMLBIBLE biblename="King James Version">
  <BIBLEBOOK bnumber="1" bname="Genesis" bsname="Gen">
    <CHAPTER cnumber="1">
      <VERS vnumber="1">In the beginning God created...</VERS>
      <VERS vnumber="2">Now the earth was formless...</VERS>
    </CHAPTER>
    <CHAPTER cnumber="2">
      ...
    </CHAPTER>
  </BIBLEBOOK>
  <BIBLEBOOK bnumber="2" bname="Exodus" bsname="Exod">
    ...
  </BIBLEBOOK>
</XMLBIBLE>

If your XML uses different tag/attribute names (OSIS, USFX, ThML, etc.),
you only need to change the constants in the CONFIG section below and,
if needed, the small parsing logic in `parse_books()`.

Usage:
    python xml_to_hugo.py bible.xml content/bible/
"""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# --------------------------------------------------------------------------
# CONFIG — adjust these to match your XML's actual tag/attribute names
# --------------------------------------------------------------------------
BOOK_TAG = "BIBLEBOOK"
BOOK_NAME_ATTR = "bname"       # full book name, e.g. "Genesis"
BOOK_NUMBER_ATTR = "bnumber"   # book order, e.g. "1"
BOOK_SHORTNAME_ATTR = "bsname" # abbreviation, e.g. "Gen"

CHAPTER_TAG = "CHAPTER"
CHAPTER_NUMBER_ATTR = "cnumber"

VERSE_TAG = "VERS"
VERSE_NUMBER_ATTR = "vnumber"

# Books 1-39 are Old Testament, 40-66 are New Testament in most orderings.
# Adjust if your numbering differs.
OT_MAX_BOOK_NUMBER = 39
# --------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Turn 'Song of Solomon' into 'song-of-solomon'."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def escape_front_matter_string(value: str) -> str:
    """Escape double quotes for safe use inside YAML front matter."""
    return value.replace('"', '\\"')


def parse_books(xml_path: Path):
    """Yields a dict per book: {number, name, shortname, chapters}."""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for book_el in root.iter(BOOK_TAG):
        number = int(book_el.get(BOOK_NUMBER_ATTR))
        name = book_el.get(BOOK_NAME_ATTR)
        shortname = book_el.get(BOOK_SHORTNAME_ATTR, name)

        chapters = []
        for chapter_el in book_el.findall(CHAPTER_TAG):
            chapter_number = chapter_el.get(CHAPTER_NUMBER_ATTR)
            verses = []
            for verse_el in chapter_el.findall(VERSE_TAG):
                verse_number = verse_el.get(VERSE_NUMBER_ATTR)
                verse_text = (verse_el.text or "").strip()
                verses.append((verse_number, verse_text))
            chapters.append((chapter_number, verses))

        yield {
            "number": number,
            "name": name,
            "shortname": shortname,
            "chapters": chapters,
        }


def render_markdown(book: dict) -> str:
    """Build the full Markdown file content (front matter + body) for a book."""
    testament = "Old Testament" if book["number"] <= OT_MAX_BOOK_NUMBER else "New Testament"

    front_matter = "\n".join([
        "---",
        f'title: "{escape_front_matter_string(book["name"])}"',
        f'short_name: "{escape_front_matter_string(book["shortname"])}"',
        f'testament: "{testament}"',
        f'weight: {book["number"]}',
        f'book_number: {book["number"]}',
        "---",
        "",
    ])

    body_lines = []
    for chapter_number, verses in book["chapters"]:
        body_lines.append(f"## Chapter {chapter_number}\n")
        for verse_number, verse_text in verses:
            body_lines.append(f"{verse_number}. {verse_text}")
        body_lines.append("")  # blank line between chapters

    return front_matter + "\n".join(body_lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml_file", type=Path, help="Path to the source Bible XML file")
    parser.add_argument("output_dir", type=Path, help="Hugo content directory to write into, e.g. content/bible")
    args = parser.parse_args()

    if not args.xml_file.exists():
        sys.exit(f"XML file not found: {args.xml_file}")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for book in parse_books(args.xml_file):
        slug = slugify(book["name"])
        out_path = args.output_dir / f"{slug}.md"
        out_path.write_text(render_markdown(book), encoding="utf-8")
        print(f"Wrote {out_path}  ({len(book['chapters'])} chapters)")
        count += 1

    print(f"\nDone. Generated {count} book pages in {args.output_dir}/")


if __name__ == "__main__":
    main()
