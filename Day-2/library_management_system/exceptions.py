class LibraryError(Exception):
    """Base exception for all library-related errors."""


class BookNotFoundError(LibraryError):
    """Raised when a requested book does not exist."""


class UserNotFoundError(LibraryError):
    """Raised when a requested user does not exist."""


class DuplicateBookIDError(LibraryError):
    """Raised when a duplicate book ID is used."""


class DuplicateUserIDError(LibraryError):
    """Raised when a duplicate user ID is used."""


class BookUnavailableError(LibraryError):
    """Raised when an unavailable book is issued."""


class BookAlreadyAvailableError(LibraryError):
    """Raised when returning a book that is not issued."""


class BookIssuedError(LibraryError):
    """Raised when trying to remove an issued book."""