from book import Book
from user import User
from exceptions import (
    BookNotFoundError,
    UserNotFoundError,
    BookUnavailableError,
    DuplicateIDError,
)


class Library:
    """
    Object-Oriented Library System orchestrating books and users.
    """

    def __init__(self) -> None:
        self.books: dict[int, Book] = {}
        self.users: dict[int, User] = {}

    def add_book(self, book_id: int, title: str, author: str) -> None:
        """Add a new book to library catalog."""
        if book_id in self.books:
            raise DuplicateIDError("Book ID already exists.")
        book = Book(book_id, title, author)
        self.books[book_id] = book
        print("Book added successfully.")

    def remove_book(self, book_id: int) -> None:
        """Remove a book from library catalog."""
        if book_id not in self.books:
            raise BookNotFoundError("Book ID not found.")
        del self.books[book_id]
        print("Book removed successfully.")

    def search_book(self, keyword: str) -> list[Book]:
        """Search books by title or author keyword."""
        kw = keyword.lower().strip()
        results = []
        for book in self.books.values():
            if kw in book.title.lower() or kw in book.author.lower():
                results.append(book)
        return results

    def register_user(self, user_id: int, name: str) -> None:
        """Register a new library user."""
        if user_id in self.users:
            raise DuplicateIDError("User ID already registered.")
        user = User(user_id, name)
        self.users[user_id] = user
        print("User registered successfully.")

    def issue_book(self, book_id: int, user_id: int) -> None:
        """Issue an available book to a registered user."""
        if book_id not in self.books:
            raise BookNotFoundError("Book ID not found.")
        if user_id not in self.users:
            raise UserNotFoundError("User ID not registered.")

        book = self.books[book_id]
        if not book.is_available:
            raise BookUnavailableError("Book is currently unavailable/issued.")

        book.issue_to(user_id)
        print("Book issued successfully.")

    def return_book(self, book_id: int) -> None:
        """Return an issued book to library."""
        if book_id not in self.books:
            raise BookNotFoundError("Book ID not found.")

        book = self.books[book_id]
        if book.is_available:
            print("Book is already in the library.")
            return

        book.return_to_library()
        print("Book returned successfully.")

    def list_available_books(self) -> list[Book]:
        """Return list of available books."""
        return [b for b in self.books.values() if b.is_available]

    def list_issued_books(self) -> list[Book]:
        """Return list of checked out books."""
        return [b for b in self.books.values() if not b.is_available]
