
def add_contact(contacts: list[dict], name: str, phone: str, email: str) -> None:
    """
    Add a new contact.

    Args:
        contacts: List containing all contacts.
        name: Name of the contact.
        phone: Phone number of the contact.
        email: Email address of the contact.

    Raises:
        ValueError: If phone or email is empty.
        ValueError: If the contact already exists.
    """

    if not phone:
        raise ValueError("Phone number cannot be empty.")

    if not email:
        raise ValueError("Email cannot be empty.")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            raise ValueError("Contact already exists.")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })


def delete_contact(contacts: list[dict], name: str) -> None:
    """
    Delete a contact by name.

    Args:
        contacts: List containing all contacts.
        name: Name of the contact to delete.

    Raises:
        ValueError: If the contact is not found.
    """

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            return

    raise ValueError("Contact not found.")


def search_contact(contacts: list[dict], name: str) -> dict:
    """
    Search for a contact by name.

    Args:
        contacts: List containing all contacts.
        name: Name of the contact to search.

    Returns:
        The matching contact.

    Raises:
        ValueError: If the contact is not found.
    """

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    raise ValueError("Contact not found.")


def update_contact(
    contacts: list[dict],
    name: str,
    phone: str,
    email: str
) -> None:
    """
    Update an existing contact.

    Args:
        contacts: List containing all contacts.
        name: Name of the contact to update.
        phone: New phone number.
        email: New email address.

    Raises:
        ValueError: If phone or email is empty.
        ValueError: If the contact is not found.
    """

    if not phone:
        raise ValueError("Phone number cannot be empty.")

    if not email:
        raise ValueError("Email cannot be empty.")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = phone
            contact["email"] = email
            return

    raise ValueError("Contact not found.")


def list_contacts(contacts: list[dict]) -> None:
    """
    Display all contacts.

    Args:
        contacts: List containing all contacts.
    """

    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print()