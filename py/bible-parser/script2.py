from bs4 import BeautifulSoup
from pathlib import Path
import os
import glob
# defaultdict makes dictionaries less painful by automatically assigning default values
# to new keys
from collections import defaultdict

SOURCE_FILE = Path("./engDRA_vpl.xml")
OUTPUT_DIR = Path("../../content/projects/bible/dr/")

def main():
    books = parse_verses(SOURCE_FILE)

    for book in books:
        write_md(books[book])

def parse_verses(xml_path):
    soup = BeautifulSoup(xml_path.read_text(), "xml")
    books = defaultdict(list)

    for verse in soup.find_all("v"):
        books[verse["b"]].append({
            # this makes eg. book_chapter = "JOB-42"
            "book_chapter": f"{verse["b"]}-{verse["c"].zfill(2)}",
            "book": verse["b"],
            "chapter": verse["c"],
            "verse": verse["v"],
            "text": verse.string,
        })
    return books

def write_md(verses):
    parsed_chapters = []
    target_file = ""
    count = 1
    for v in verses:
        lines = []
        # make necessary directory if it doesnt exist
        os.makedirs(OUTPUT_DIR / v["book"], exist_ok=True)
        # if new book chapter is encountered
        if v["book_chapter"] not in parsed_chapters:
            count = count + 1
            # create _index file in dir
            (OUTPUT_DIR / f"{v["book"]}/_index.md").write_text(f"---\ndraft: false\ntitle: '{v["book"]}'\nweight: 1\n---")
            # add frontmatter to lines
            lines.append(f"---\ndraft: false\ntitle: '{v["book"]} {v["chapter"]}'\nweight: {v["chapter"]}\n---")
            # file to write to
            target_file = f"{v["chapter"]}.md"
            # delete file if it exists
            try:
                os.remove(OUTPUT_DIR / v["book"] / target_file)
            except OSError:
                pass
            # append new chapter to list of parsed chapters
            parsed_chapters.append(v["book_chapter"])
        if "." in v["text"]:
            newline = "\n\n"
        else:
            newline = ""
            
        lines.append(f"^{v["verse"]}{v["text"]}{newline}")

        with (OUTPUT_DIR / v["book"] / target_file).open("a") as f:
            f.write("\n".join(lines))

main()
