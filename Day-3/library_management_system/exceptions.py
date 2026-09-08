class LibraryError(Exception):
    """Base exception class for library management system."""
    pass


class BookNotFoundError(LibraryError):
    """Raised when a book ID is not found in the catalog."""
    pass


class UserNotFoundError(LibraryError):
    """Raised when a user ID is not registered in the system."""
    pass


class BookUnavailableError(LibraryError):
    """Raised when trying to issue a book that is already checked out."""
    pass


class DuplicateIDError(LibraryError):
    """Raised when adding a book or user with an existing ID."""
    pass


class InvalidInputError(LibraryError):
    """Raised when input validation fails."""
    pass
