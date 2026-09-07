

def add_to_cart(
    cart: list[dict],
    products: list[dict],
    product_id: int,
    quantity: int
) -> None:
    """
    Add a product to the cart.

    Args:
        cart: List containing cart items.
        products: List containing available products.
        product_id: ID of the product to add.
        quantity: Number of products to add.

    Raises:
        ValueError: If the product does not exist.
        ValueError: If quantity is not positive.
    """

    if quantity <= 0:
        raise ValueError("Quantity must be positive.")

    product = None

    for item in products:
        if item["id"] == product_id:
            product = item
            break

    if product is None:
        raise ValueError("Product does not exist.")

    cart.append({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })


def remove_from_cart(
    cart: list[dict],
    product_id: int
) -> None:
    """
    Remove a product from the cart.

    Args:
        cart: List containing cart items.
        product_id: ID of the product to remove.

    Raises:
        ValueError: If the product is not in the cart.
    """

    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            return

    raise ValueError("Product is not in the cart.")


def calculate_subtotal(cart: list[dict]) -> float:
    """
    Calculate the cart subtotal.

    Args:
        cart: List containing cart items.

    Returns:
        The total price before discount and tax.
    """

    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal: float) -> float:
    """
    Calculate discount based on the subtotal.

    Args:
        subtotal: Cart subtotal.

    Returns:
        The discount amount.

    Rules:
        10% discount if subtotal is 50000 or more.
        Otherwise, no discount.
    """

    if subtotal >= 50000:
        return subtotal * 0.10

    return 0


def calculate_tax(amount: float) -> float:
    """
    Calculate tax on the amount after discount.

    Args:
        amount: Amount after discount.

    Returns:
        The tax amount.
    """

    return amount * 0.18


def calculate_final_amount(cart: list[dict]) -> float:
    """
    Calculate the final amount including discount and tax.

    Args:
        cart: List containing cart items.

    Returns:
        The final amount to pay.
    """

    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount)

    return amount_after_discount + tax
