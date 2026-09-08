class Contact:
    """
    Represents a personal/professional contact record.
    """

    def __init__(self, name: str, phone: str, email: str) -> None:
        if not name or not name.strip():
            raise ValueError("Contact name cannot be empty.")
        if not phone or not phone.strip():
            raise ValueError("Phone number cannot be empty.")
        if not email or not email.strip():
            raise ValueError("Email cannot be empty.")

        self.name: str = name.strip()
        self.phone: str = phone.strip()
        self.email: str = email.strip()

    def update_details(self, phone: str, email: str) -> None:
        """Update phone number and email address with validation."""
        if not phone or not phone.strip():
            raise ValueError("Phone number cannot be empty.")
        if not email or not email.strip():
            raise ValueError("Email cannot be empty.")

        self.phone = phone.strip()
        self.email = email.strip()

    def to_dict(self) -> dict[str, str]:
        """Convert contact details to a dictionary."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    def __str__(self) -> str:
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
