class PasswordValidator:
    """
    Object-Oriented Password Policy Validator.
    """

    def __init__(self, min_length: int = 8) -> None:
        self.min_length: int = min_length

    def validate(self, password: str) -> list[str]:
        """
        Validate password against set policy requirements.
        Returns list of failure messages, or an empty list if valid.
        """
        errors = []

        if len(password) < self.min_length:
            errors.append(f"Missing minimum {self.min_length} characters.")

        if not any(char.isupper() for char in password):
            errors.append("Missing uppercase letter.")

        if not any(char.islower() for char in password):
            errors.append("Missing lowercase letter.")

        if not any(char.isdigit() for char in password):
            errors.append("Missing number.")

        if not any(not char.isalnum() for char in password):
            errors.append("Missing special character.")

        return errors
