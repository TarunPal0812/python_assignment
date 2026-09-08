from validator import PasswordValidator


def main() -> None:
    password = input("Password: ")

    validator = PasswordValidator(min_length=8)
    errors = validator.validate(password)

    if not errors:
        print("Valid password.")
    else:
        print("Invalid password:")
        for error in errors:
            print("-", error)


if __name__ == "__main__":
    main()
