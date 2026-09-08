from contact import Contact
from manager import ContactManager


def main() -> None:
    initial_contact = Contact("Tarun", "9876543210", "tarun@example.com")
    manager = ContactManager([initial_contact])

    try:
        manager.add_contact("Ashmita", "9876543211", "ashmita@example.com")

        print("All Contacts:")
        manager.list_contacts()

        found = manager.search_contact("Tarun")
        print("Search Result:")
        print(found)
        print()

        manager.update_contact("Tarun", "9999999999", "newtarun@example.com")
        print("After Update:")
        manager.list_contacts()

        manager.delete_contact("Ashmita")
        print("After Delete:")
        manager.list_contacts()

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()


