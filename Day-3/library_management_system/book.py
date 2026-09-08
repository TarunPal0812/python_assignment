class Book:
    """
    Represents a book entry in the library catalog.
    """

    def __init__(self, book_id: int, title: str, author: str) -> None:
        self.book_id: int = book_id
        self.title: str = title.strip()
        self.author: str = author.strip()
        self.is_available: bool = True
        self.issued_to: int | None = None

    def issue_to(self, user_id: int) -> None:
        """Mark book as issued to specified user ID."""
        self.is_available = False
        self.issued_to = user_id

    def return_to_library(self) -> None:
        """Mark book as returned and available."""
        self.is_available = True
        self.issued_to = None

    def to_dict(self) -> dict:
        """Convert book object to dictionary representation."""
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.is_available,
            "issued_to": self.issued_to,
        }
