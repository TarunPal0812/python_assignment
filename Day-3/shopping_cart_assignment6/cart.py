from product import Product, CartItem


class ShoppingCart:
    """
    Manages customer shopping cart, discounts, taxes, and order total calculation.
    """

    DISCOUNT_THRESHOLD: float = 50000.0
    DISCOUNT_RATE: float = 0.10
    TAX_RATE: float = 0.18

    def __init__(self, catalog: list[Product]) -> None:
        self.catalog: dict[int, Product] = {p.product_id: p for p in catalog}
        self.items: list[CartItem] = []

    def add_to_cart(self, product_id: int, quantity: int) -> None:
        """Add a product to cart by product ID."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if product_id not in self.catalog:
            raise ValueError("Product does not exist.")

        product = self.catalog[product_id]

        # Check if already in cart
        for item in self.items:
            if item.product.product_id == product_id:
                item.quantity += quantity
                return

        self.items.append(CartItem(product, quantity))

    def remove_from_cart(self, product_id: int) -> None:
        """Remove a product from cart."""
        for item in self.items:
            if item.product.product_id == product_id:
                self.items.remove(item)
                return
        raise ValueError("Product is not in the cart.")

    def calculate_subtotal(self) -> float:
        """Calculate total price of all items before discount and tax."""
        return sum(item.get_total_price() for item in self.items)

    def calculate_discount(self, subtotal: float) -> float:
        """Calculate discount based on subtotal."""
        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE
        return 0.0

    def calculate_tax(self, amount: float) -> float:
        """Calculate tax on net amount."""
        return amount * self.TAX_RATE

    def calculate_final_amount(self) -> float:
        """Calculate final payable amount."""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        taxable_amount = subtotal - discount
        tax = self.calculate_tax(taxable_amount)
        return taxable_amount + tax

    def display_bill(self) -> None:
        """Print itemized receipt breakdown."""
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item.product.name} - Quantity: {item.quantity} - ₹ {item.get_total_price():g}")

        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        tax = self.calculate_tax(subtotal - discount)
        final_amount = self.calculate_final_amount()

        print()
        print(f"Subtotal: ₹ {subtotal:g}")
        print(f"Discount: ₹ {discount:g}")
        print(f"Tax: ₹ {tax:g}")
        print(f"Final Amount: ₹ {final_amount:g}")
