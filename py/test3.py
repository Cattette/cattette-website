from bs4 import BeautifulSoup

book = ''
books = []

with open('./engDRA_vpl.xml', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, "xml")

verses = soup.find_all('v')

# iterate over all verse tags to create a single list of all books
for verse in verses:
    if verse['b'] != book:
        book = verse['b']
        books.append(book)
    verse_str = verse.string

for book in books:
    with open("books/" + book + ".md", "w") as f:
        f.write('# ' + book + '\n')
        for verse in verses:
            if verse['b'] == book:
                f.write(verse['v'] + verse.string + '\n \n')

# print(books)
