from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"[EMAIL] Sent to {recipient}: {message}")


class SMSNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] Sent to {recipient}: {message}")


class UserService:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def register_user(self, username: str, contact: str) -> None:
        print(f"\nUser '{username}' registered successfully in database.")
        self.notifier.send(contact, f"Welcome to the platform, {username}!")


def main() -> None:

    email_service = UserService(notifier=EmailNotifier())
    email_service.register_user("Tarun", "tarun@example.com")

    sms_service = UserService(notifier=SMSNotifier())
    sms_service.register_user("Pritam", "+91-9876543210")


if __name__ == "__main__":
    main()


# Output

# User 'Tarun' registered successfully in database.
# [EMAIL] Sent to tarun@example.com: Welcome to the platform, Tarun!

# User 'Ashmita' registered successfully in database.
# [SMS] Sent to +91-9876543210: Welcome to the platform, Pritam!