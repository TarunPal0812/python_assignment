import sys
from product import Product
from cart import ShoppingCart

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    catalog = [
        Product(1, "Laptop", 70000),
        Product(2, "Mouse", 1200),
        Product(3, "Keyboard", 2500),
    ]

    cart = ShoppingCart(catalog)

    try:
        cart.add_to_cart(1, 1)
        cart.add_to_cart(2, 2)
        cart.add_to_cart(3, 1)

        cart.display_bill()

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
