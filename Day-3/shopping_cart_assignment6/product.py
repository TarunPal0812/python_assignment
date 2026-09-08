class Product:
    """
    Represents an item available in store catalog.
    """

    def __init__(self, product_id: int, name: str, price: float) -> None:
        if product_id <= 0:
            raise ValueError("Product ID must be positive.")
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.product_id: int = product_id
        self.name: str = name.strip()
        self.price: float = float(price)


class CartItem:
    """
    Represents a line item inside the ShoppingCart.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self.product: Product = product
        self.quantity: int = quantity

    def get_total_price(self) -> float:
        """Calculate line item total price."""
        return self.product.price * self.quantity
