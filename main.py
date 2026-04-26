from add_book import add_book
from display_books import display_books
from issue_book import issue_book
from return_book import return_book
from search_book import search_book

library = []

def main():
    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        choice = int(input("Enter your choice(1-6): "))

        if choice == '1':
            add_book(library)
        elif choice == '2':
            display_books(library)
        elif choice == '3':
            issue_book(library)
        elif choice == '4':
            return_book(library)
        elif choice == '5':
            search_book(library)
        elif choice == '6':
            print(" Exiting...")
            break
        else:
            print(" Invalid choice!")

main()