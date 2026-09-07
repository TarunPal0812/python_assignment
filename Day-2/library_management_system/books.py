
from exceptions import (
    BookNotFoundError,
    DuplicateBookIDError,
    BookIssuedError
)


Book = dict[str, int | str | bool | None]


books: list[Book] = [
    {
        "id": 1,
        "title": "Inglorious Empire",
        "author": "Sashi Tharoor",
        "available": True,
        "issued_to": None
    }
]


def add_book(book_id: int, title: str, author: str) -> None:
    """
    Add a new book to the library.

    Args:
        book_id: Unique ID of the book.
        title: Title of the book.
        author: Name of the book's author.

    Raises:
        DuplicateBookIDError: If the book ID already exists.
    """

    for book in books:
        if book["id"] == book_id:
            raise DuplicateBookIDError(
                "Book ID already exists."
            )

    new_book: Book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True,
        "issued_to": None
    }

    books.append(new_book)

    print("Book added successfully.")


def find_book(book_id: int) -> Book:
    """
    Find a book using its unique ID.

    Args:
        book_id: ID of the book to search for.

    Returns:
        The matching book dictionary.

    Raises:
        BookNotFoundError: If no book exists with the given ID.
    """

    for book in books:
        if book["id"] == book_id:
            return book

    raise BookNotFoundError("Book not found.")


def remove_book(book_id: int) -> None:
    """
    Remove a book from the library.

    An issued book cannot be removed.

    Args:
        book_id: ID of the book to remove.

    Raises:
        BookNotFoundError: If the book does not exist.
        BookIssuedError: If the book is currently issued.
    """

    book: Book = find_book(book_id)

    if not book["available"]:
        raise BookIssuedError(
            "Cannot remove an issued book."
        )

    books.remove(book)

    print("Book removed successfully.")


def search_book(keyword: str) -> list[Book]:
    """
    Search for books by title or author.

    Args:
        keyword: Text to search for.

    Returns:
        A list of matching books.
    """

    keyword = keyword.lower()

    results: list[Book] = []

    for book in books:

        title = str(book["title"]).lower()
        author = str(book["author"]).lower()

        if keyword in title or keyword in author:
            results.append(book)

    return results


def list_available_books() -> list[Book]:
    """
    Get all currently available books.

    Returns:
        A list of available books.
    """

    return [
        book
        for book in books
        if book["available"] is True
    ]


def list_issued_books() -> list[Book]:
    """
    Get all currently issued books.

    Returns:
        A list of issued books.
    """

    return [
        book
        for book in books
        if book["available"] is False
    ]