from exceptions import (
    UserNotFoundError,
    DuplicateUserIDError
)


User = dict[str, int | str]


users: list[User] = [
    {
        "id": 1,
        "name": "Pritam"
    }
]


def register_user(user_id: int, name: str) -> None:
    """
    Register a new user in the library.

    Args:
        user_id: Unique ID for the user.
        name: Name of the user.

    Raises:
        DuplicateUserIDError: If the user ID already exists.
    """

    for user in users:

        if user["id"] == user_id:
            raise DuplicateUserIDError(
                "User ID already exists."
            )

    new_user: User = {
        "id": user_id,
        "name": name
    }

    users.append(new_user)

    print("User registered successfully.")


def find_user(user_id: int) -> User:
    """
    Find a user using their unique ID.

    Args:
        user_id: ID of the user.

    Returns:
        The matching user dictionary.

    Raises:
        UserNotFoundError: If the user does not exist.
    """

    for user in users:

        if user["id"] == user_id:
            return user

    raise UserNotFoundError(
        "User not found."
    )