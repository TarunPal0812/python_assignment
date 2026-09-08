class InventoryError(Exception):
    """Base exception class for inventory management operations."""
    pass


class ProductNotFoundError(InventoryError):
    """Raised when a product does not exist in inventory."""
    pass


class NegativeStockError(InventoryError):
    """Raised when stock quantity is set to a negative value."""
    pass


class InsufficientStockError(InventoryError):
    """Raised when sell request exceeds available stock."""
    pass
