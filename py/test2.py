
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def parse_book(xml_path: Path):
    print("parsing:", xml_path)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    for book_el in root.iter("v"):
        book = str(book_el.get("b"))
        chapter = int(book_el.get("c"))
        verse = int(book_el.get("v"))
        print(root.findall("v"))

    # return {
    #     "chapter": chapter,
    #     "verse": verse,
    # }

parse_book("./engDRA_vpl.xml")
# def render_book (book: dict) -> str:
    
