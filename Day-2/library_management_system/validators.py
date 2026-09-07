def get_positive_int(message: str) -> int:
    """
    Get a valid positive integer from the user.

    Args:
        message: Message displayed to the user.

    Returns:
        A positive integer entered by the user.
    """

    while True:
        try:
            value: int = int(input(message))

            if value <= 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_non_empty_string(message: str) -> str:
    """
    Get a non-empty string from the user.

    Args:
        message: Message displayed to the user.

    Returns:
        A non-empty string entered by the user.
    """

    while True:
        value: str = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")