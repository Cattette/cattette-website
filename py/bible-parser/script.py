from bs4 import BeautifulSoup
from pathlib import Path
# defaultdict makes dictionaries less painful by automatically assigning default values
# to new keys
from collections import defaultdict

SOURCE_FILE = Path("./engDRA_vpl.xml")
OUTPUT_DIR = Path("../../content/projects/bible/dr/")

def parse_verses(xml_path):
    soup = BeautifulSoup(xml_path.read_text(), "xml")
    books = defaultdict(list)

    for verse in soup.find_all("v"):
        books[verse["b"]].append({
            "chapter": verse["c"],
            "verse": verse["v"],
            "text": verse.string,
        })
    return books

def write_md(book_id, book, verses, output_dir):
    lines = []
    current_chapter = None
    # increment book ID 
    book_id = book_id + 1

    lines.append(f"---\ndraft: false\ntitle: '{book_id} {book}'\nweight: {book_id}\n---")

    # add leading 0 to lower values
    # if book_id < 10:
    #     book_id = (f"0{book_id}")
    # create frontmatter    

    for v in verses:
        # add chapter title if chapter changes
        if v["chapter"] != current_chapter:
            current_chapter = v["chapter"]
            lines.append(f"# {book} {current_chapter}\n")
        # add verse
        lines.append(f"^{v["verse"]} {v["text"]}\n")
    # write lines var to output file
    (output_dir / f"{book}.md").write_text("\n".join(lines), encoding="utf-8" )
    # return book_id as a int so we can re-input it into this
    # function and increment it further
    return int(book_id)

book_id = 0
books = parse_verses(SOURCE_FILE)
for book, verses in books.items():
    book_id = write_md(book_id, book, verses, OUTPUT_DIR)

    

