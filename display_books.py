def display_books(library):
    if len(library) == 0:
        print(" No books available")
        return

    print("\n Library Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}")