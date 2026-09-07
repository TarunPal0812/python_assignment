# 4. Contact Manager 
# contacts = [ 
#     { 
#         "name": "Tarun", 
#         "phone": "9876543210", 
#         "email": "tarun@example.com" 
#     } 
# ] 
# Implement: 
# add_contact() 
# delete_contact() 
# search_contact() 
# update_contact() 
# list_contacts() 
# Requirements 
# ● Phone number cannot be empty 
# ● Email cannot be empty 
# ● Duplicate contacts should be rejected 
# ● Searching for a missing contact should produce a meaningful error 
# ● Split the program into modules 


from utils import (
    add_contact,
    delete_contact,
    search_contact,
    update_contact,
    list_contacts
)


def main() -> None:
    """
    Run the contact manager program.
    """

    contacts = [
        {
            "name": "Tarun",
            "phone": "9876543210",
            "email": "tarun@example.com"
        }
    ]

    try:
    
        add_contact(
            contacts,
            "Ashmita",
            "9876543211",
            "ashmita@example.com"
        )

    
        print("All Contacts:")
        list_contacts(contacts)

     
        contact = search_contact(contacts, "Tarun")

        print("Search Result:")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print()

    
        update_contact(
            contacts,
            "Tarun",
            "9999999999",
            "newtarun@example.com"
        )

        print("After Update:")
        list_contacts(contacts)

       
        delete_contact(contacts, "Ashmita")

        print("After Delete:")
        list_contacts(contacts)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()


# Output

# Search Result:
# Name: Tarun
# Phone: 9876543210
# Email: tarun@example.com

# After Update:
# Name: Tarun
# Phone: 9999999999
# Email: newtarun@example.com

# Name: Ashmita
# Phone: 9876543211
# Email: ashmita@example.com

# After Delete:
# Name: Tarun
# Phone: 9999999999
# Email: newtarun@example.com