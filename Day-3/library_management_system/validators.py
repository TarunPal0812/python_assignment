from exceptions import InvalidInputError


def get_positive_int(prompt: str) -> int:
    """Prompt user and return a positive integer."""
    try:
        val = int(input(prompt).strip())
        if val <= 0:
            raise InvalidInputError("ID must be a positive integer.")
        return val
    except ValueError:
        raise InvalidInputError("Invalid input. Please enter an integer.")


def get_non_empty_string(prompt: str) -> str:
    """Prompt user and return a non-empty string."""
    val = input(prompt).strip()
    if not val:
        raise InvalidInputError("Input string cannot be empty.")
    return val
