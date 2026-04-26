def issue_book(library):
    book_id = input("Enter Book ID to issue: ")

    for book in library:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                print(" Book issued successfully!")
                return
            else:
                print(" Book already issued!")
                return

    print(" Book not found!")