books = [
    {"title": "The Hobbit", "authorName": "J.R.R. Tolkien", "releaseYear": 1937},
    {"title": "1984", "authorName": "George Orwell", "releaseYear": 1949},
    {"title": "To Kill a Mockingbird", "authorName": "Harper Lee", "releaseYear": 1960},
]


def sort_by_year(book):
    return book["releaseYear"]


filtered_books = [book for book in books if book["releaseYear"] <= 1950]

filtered_books.sort(key=sort_by_year)

print(filtered_books)