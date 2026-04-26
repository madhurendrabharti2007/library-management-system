def return_book(library):
    book_id = input("Enter Book ID to return: ")

    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                print(" Book returned successfully!")
                return
            else:
                print(" Book was not issued!")
                return

    print(" Book not found!")