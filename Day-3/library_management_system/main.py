from library import Library
from book import Book
from validators import get_positive_int, get_non_empty_string
from exceptions import LibraryError


def display_books(book_list: list[Book]) -> None:
    """Display a list of Book objects in a readable format."""
    if not book_list:
        print("No books found.")
        return

    print("\n" + "-" * 50)
    for book in book_list:
        status = "Available" if book.is_available else "Issued"
        print(f"ID: {book.book_id}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Status: {status}")
        if not book.is_available:
            print(f"Issued To User ID: {book.issued_to}")
        print("-" * 50)


def show_menu() -> None:
    """Display Library System menu."""
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Register User")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. List Available Books")
    print("8. List Issued Books")
    print("9. Exit")


def main() -> None:
    library = Library()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                book_id = get_positive_int("Enter Book ID: ")
                title = get_non_empty_string("Enter Book Title: ")
                author = get_non_empty_string("Enter Author Name: ")
                library.add_book(book_id, title, author)

            elif choice == "2":
                book_id = get_positive_int("Enter Book ID: ")
                library.remove_book(book_id)

            elif choice == "3":
                keyword = get_non_empty_string("Enter title or author: ")
                results = library.search_book(keyword)
                display_books(results)

            elif choice == "4":
                user_id = get_positive_int("Enter User ID: ")
                name = get_non_empty_string("Enter User Name: ")
                library.register_user(user_id, name)

            elif choice == "5":
                book_id = get_positive_int("Enter Book ID: ")
                user_id = get_positive_int("Enter User ID: ")
                library.issue_book(book_id, user_id)

            elif choice == "6":
                book_id = get_positive_int("Enter Book ID: ")
                library.return_book(book_id)

            elif choice == "7":
                available = library.list_available_books()
                display_books(available)

            elif choice == "8":
                issued = library.list_issued_books()
                display_books(issued)

            elif choice == "9":
                print("Thank you for using the Library Management System.")
                break

            else:
                print("Invalid menu choice. Please select between 1 and 9.")

        except LibraryError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
