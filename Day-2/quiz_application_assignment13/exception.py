
class QuizError(Exception):
    """Base exception for quiz-related errors."""


class InvalidAnswerError(QuizError):
    """Raised when the user enters an invalid answer."""


