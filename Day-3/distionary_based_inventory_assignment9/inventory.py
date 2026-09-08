from exceptions import (
    ProductNotFoundError,
    NegativeStockError,
    InsufficientStockError,
)


class InventoryManager:
    """
    Object-Oriented Inventory Management engine with custom exception controls.
    """

    def __init__(self, initial_stock: dict[str, int] | None = None) -> None:
        self.inventory: dict[str, int] = (
            initial_stock.copy() if initial_stock is not None else {}
        )

    def add_product(self, product: str, quantity: int) -> None:
        """Add a new product with stock quantity to inventory."""
        if quantity < 0:
            raise NegativeStockError("Product stock cannot be negative.")
        self.inventory[product] = quantity

    def remove_product(self, product: str) -> None:
        """Remove a product completely from inventory."""
        if product not in self.inventory:
            raise ProductNotFoundError("Product does not exist.")
        del self.inventory[product]

    def sell_product(self, product: str, quantity: int) -> None:
        """Sell specified quantity of product."""
        if product not in self.inventory:
            raise ProductNotFoundError("Cannot sell a nonexistent product.")
        if quantity > self.inventory[product]:
            raise InsufficientStockError("Not enough stock available.")
        self.inventory[product] -= quantity

    def restock_product(self, product: str, quantity: int) -> None:
        """Restock an existing product in inventory."""
        if product not in self.inventory:
            raise ProductNotFoundError("Cannot restock a nonexistent product.")
        if quantity < 0:
            raise NegativeStockError("Restock quantity cannot be negative.")
        self.inventory[product] += quantity

    def check_stock(self, product: str) -> int:
        """Check current stock level for product."""
        if product not in self.inventory:
            raise ProductNotFoundError("Product does not exist.")
        return self.inventory[product]

    def get_inventory(self) -> dict[str, int]:
        """Return a copy of the inventory dictionary."""
        return self.inventory.copy()
