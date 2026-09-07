def validate_password(password: str) -> list[str]:
    """
    Validate a password based on the required rules.

    Args:
        password: The password to validate.

    Returns:
        A list containing all validation errors.
        Returns an empty list if the password is valid.
    """

    errors = []

    if len(password) < 8:
        errors.append("Missing minimum 8 characters.")

    if not any(char.isupper() for char in password):
        errors.append("Missing uppercase letter.")

    if not any(char.islower() for char in password):
        errors.append("Missing lowercase letter.")

    if not any(char.isdigit() for char in password):
        errors.append("Missing number.")

    if not any(not char.isalnum() for char in password):
        errors.append("Missing special character.")

    return errors