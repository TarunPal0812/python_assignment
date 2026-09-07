from books import Book, find_book
from users import find_user

from exceptions import (
    BookUnavailableError,
    BookAlreadyAvailableError
)


def issue_book(book_id: int, user_id: int) -> None:
    """
    Issue an available book to a registered user.

    Args:
        book_id: ID of the book to issue.
        user_id: ID of the user receiving the book.

    Raises:
        BookNotFoundError: If the book does not exist.
        UserNotFoundError: If the user does not exist.
        BookUnavailableError: If the book is already issued.
    """

    book: Book = find_book(book_id)

    
    find_user(user_id)

    if not book["available"]:
        raise BookUnavailableError(
            "Book is currently unavailable."
        )

    book["available"] = False
    book["issued_to"] = user_id

    print("Book issued successfully.")


def return_book(book_id: int) -> None:
    """
    Return an issued book to the library.

    Args:
        book_id: ID of the book being returned.

    Raises:
        BookNotFoundError: If the book does not exist.
        BookAlreadyAvailableError: If the book was not issued.
    """

    book: Book = find_book(book_id)

    if book["available"]:
        raise BookAlreadyAvailableError(
            "This book is not currently issued."
        )

    book["available"] = True
    book["issued_to"] = None

    print("Book returned successfully.")