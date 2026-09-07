# 5. Password Validator 
# Create: 
# validate_password(password) 
# Password requirements: 
# ● Minimum 8 characters 
# ● At least one uppercase 
# ● At least one lowercase 
# ● At least one number 
# ● At least one special character 
# Example: 
# Password: Hello123 
# Output: 
# Invalid password: - Missing special character

from utils import validate_password

def main() -> None:
    """
    Read a password and display its validation result.
    """

    password = input("Password: ")

    errors = validate_password(password)

    if not errors:
        print("Valid password.")

    else:
        print("Invalid password:")

        for error in errors:
            print("-", error)


if __name__ == "__main__":
    main()