
class ProductNotFoundError(Exception):
    """Raised when a product does not exist."""

    pass


class NegativeStockError(Exception):
    """Raised when stock becomes negative."""

    pass


class InsufficientStockError(Exception):
    """Raised when there is not enough stock to sell."""

    pass