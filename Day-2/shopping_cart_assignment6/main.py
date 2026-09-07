# 6. Shopping Cart 
# Represent products as: 
# products = [ 
# {"id": 1, "name": "Laptop", "price": 70000}, 
# {"id": 2, "name": "Mouse", "price": 1200}, 
# {"id": 3, "name": "Keyboard", "price": 2500}, 
# ] 
# Implement: 
# add_to_cart() 
# remove_from_cart() 
# calculate_subtotal() 
# calculate_discount() 
# calculate_tax() 
# calculate_final_amount() 
# Rules 
# ● Product must exist 
# ● Quantity must be positive 
# ● Cannot remove something that isn't in the cart 
# ● Discount depends on total amount 
# Error Handling 
# Use exceptions for invalid cases. 

from utils import add_to_cart,calculate_discount,calculate_subtotal,calculate_final_amount,calculate_tax


products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 1200},
    {"id": 3, "name": "Keyboard", "price": 2500},
]


def main() -> None:
    """
    Add products to the cart and display the bill.
    """

    cart = []

    try:
        add_to_cart(cart, products, 1, 1)
        add_to_cart(cart, products, 2, 2)
        add_to_cart(cart, products, 3, 1)

        print("Shopping Cart:")

        for item in cart:
            total = item["price"] * item["quantity"]

            print(
                item["name"],
                "- Quantity:",
                item["quantity"],
                "- ₹",
                total
            )

        subtotal = calculate_subtotal(cart)
        discount = calculate_discount(subtotal)
        tax = calculate_tax(subtotal - discount)
        final_amount = calculate_final_amount(cart)

        print()
        print("Subtotal:", "₹", subtotal)
        print("Discount:", "₹", discount)
        print("Tax:", "₹", tax)
        print("Final Amount:", "₹", final_amount)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()


# Output

# Shopping Cart:
# Laptop - Quantity: 1 - ₹ 70000
# Mouse - Quantity: 2 - ₹ 2400
# Keyboard - Quantity: 1 - ₹ 2500

# Subtotal: ₹ 74900
# Discount: ₹ 7490.0
# Tax: ₹ 12133.8
# Final Amount: ₹ 79543.8