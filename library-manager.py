library = [
    {
        "title": "Your Next Five Moves: Master the Art of Business Strategy",
        "author": "Patrick Bet-David and Greg Dinkin",
        "about": "A book on how to plan ahead",
        "pages": 320,
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "about": "A practical book about discarding bad habits and building good ones",
        "pages": 320,
    },
    {
        "title": "Choose Your Enemies Wisely: Business Planning for the Audacious Few",
        "author": "Patrick Bet-David",
        "about": "A book that emphasizes the importance of identifying and understanding one's adversaries to succeed in the business world",
        "pages": 304,
    },
    {
        "title": "The Embedded Entrepreneur",
        "author": "Arvid Kahl",
        "about": "A book focusing on how to build an audience-driven business",
        "pages": 308,
    },
    {
        "title": "How to Be a Coffee Bean: 111 Life-Changing Ways to Create Positive Change",
        "author": "Jon Gordon",
        "about": "A book about effective ways to lead a coffee bean lifestyle",
        "pages": 256,
    },
    {
        "title": "The Creative Mindset: Mastering the Six Skills That Empower Innovation",
        "author": "Jeff DeGraff and Staney DeGraff",
        "about": "A book on how to develop creativity and  innovation skills",
        "pages": 168,
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki and Sharon Lechter",
        "about": "A book about financial literacy, financial independence, and building wealth. ",
        "pages": 336,
    },
    {
        "title": "Zero to Sold",
        "author": "Arvid Kahl",
        "about": "A book on how to bootstrap a business",
        "pages": 500,
    },
]

print("Books in the Library:\n")


def get_book_information(catalog):
    return "\n".join([f"{book['title']} by {book['author']}" for book in catalog])


print(get_book_information(library))

print("\nList of book summaries:\n")


def get_book_summaries(catalog):
    return "\n".join([book["about"] for book in catalog])


print(get_book_summaries(library))

print("\nList of books by Arvid Kahl:\n")


def get_books_by_author(catalog, author):
    return [book for book in catalog if book["author"] == author]


print(get_books_by_author(library, "Arvid Kahl"))

print("\nList of books by James Clear:\n")
print(get_books_by_author(library, "James Clear"))

print("\nTotal number of pages for all library books:\n")


def get_total_pages(books):
    return sum(book["pages"] for book in books)


print(get_total_pages(library))