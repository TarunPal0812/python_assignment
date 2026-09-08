class User:
    """
    Represents a registered library user member.
    """

    def __init__(self, user_id: int, name: str) -> None:
        self.user_id: int = user_id
        self.name: str = name.strip()

    def to_dict(self) -> dict:
        """Convert user object to dictionary representation."""
        return {
            "id": self.user_id,
            "name": self.name,
        }
