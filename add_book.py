def add_book(library):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    library.append(book)
    print(" Book added successfully!")