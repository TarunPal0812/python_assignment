from custom_exception import NegativeStockError,ProductNotFoundError,InsufficientStockError


def add_product(
    inventory: dict,
    product: str,
    quantity: int
) -> None:
    """
    Add a new product to the inventory.

    Args:
        inventory: Dictionary containing products and stock.
        product: Name of the product.
        quantity: Initial stock quantity.

    Raises:
        NegativeStockError: If quantity is negative.
    """

    if quantity < 0:
        raise NegativeStockError(
            "Product stock cannot be negative."
        )

    inventory[product] = quantity


def remove_product(
    inventory: dict,
    product: str
) -> None:
    """
    Remove a product from the inventory.

    Args:
        inventory: Dictionary containing products and stock.
        product: Name of the product to remove.

    Raises:
        ProductNotFoundError: If the product does not exist.
    """

    if product not in inventory:
        raise ProductNotFoundError(
            "Product does not exist."
        )

    del inventory[product]


def sell_product(
    inventory: dict,
    product: str,
    quantity: int
) -> None:
    """
    Sell a product and reduce its stock.

    Args:
        inventory: Dictionary containing products and stock.
        product: Name of the product.
        quantity: Number of products sold.

    Raises:
        ProductNotFoundError: If the product does not exist.
        InsufficientStockError: If there is not enough stock.
    """

    if product not in inventory:
        raise ProductNotFoundError(
            "Cannot sell a nonexistent product."
        )

    if quantity > inventory[product]:
        raise InsufficientStockError(
            "Not enough stock available."
        )

    inventory[product] -= quantity


def restock_product(
    inventory: dict,
    product: str,
    quantity: int
) -> None:
    """
    Add stock to an existing product.

    Args:
        inventory: Dictionary containing products and stock.
        product: Name of the product.
        quantity: Number of products to add.

    Raises:
        ProductNotFoundError: If the product does not exist.
    """

    if product not in inventory:
        raise ProductNotFoundError(
            "Cannot restock a nonexistent product."
        )

    inventory[product] += quantity


def check_stock(
    inventory: dict,
    product: str
) -> int:
    """
    Check the stock of a product.

    Args:
        inventory: Dictionary containing products and stock.
        product: Name of the product.

    Returns:
        Current stock quantity.

    Raises:
        ProductNotFoundError: If the product does not exist.
    """

    if product not in inventory:
        raise ProductNotFoundError(
            "Product does not exist."
        )

    return inventory[product]