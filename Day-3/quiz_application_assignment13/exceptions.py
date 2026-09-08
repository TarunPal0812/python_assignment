class QuizError(Exception):
    """Base exception for quiz application errors."""
    pass


class InvalidAnswerError(QuizError):
    """Raised when user submits an invalid answer option."""
    pass
