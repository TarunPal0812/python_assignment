from contact import Contact


class ContactManager:
    """
    Manages a repository of Contact instances.
    """

    def __init__(self, initial_contacts: list[Contact] | None = None) -> None:
        self.contacts: list[Contact] = initial_contacts if initial_contacts is not None else []

    def add_contact(self, name: str, phone: str, email: str) -> None:
        """Add a new contact after duplicate checking and validation."""
        for contact in self.contacts:
            if contact.name.lower() == name.strip().lower():
                raise ValueError("Contact already exists.")

        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)

    def delete_contact(self, name: str) -> None:
        """Delete an existing contact by name."""
        contact = self.search_contact(name)
        self.contacts.remove(contact)

    def search_contact(self, name: str) -> Contact:
        """Search and return a contact by case-insensitive name."""
        for contact in self.contacts:
            if contact.name.lower() == name.strip().lower():
                return contact
        raise ValueError("Contact not found.")

    def update_contact(self, name: str, phone: str, email: str) -> None:
        """Update existing contact info."""
        contact = self.search_contact(name)
        contact.update_details(phone, email)

    def list_contacts(self) -> None:
        """Display formatted list of all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return

        for contact in self.contacts:
            print(contact)
            print()
