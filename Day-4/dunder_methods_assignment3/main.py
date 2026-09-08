
class Money:
    def __init__(self, amount: float, currency: str = "INR") -> None:
        self.amount = round(float(amount), 2)
        self.currency = currency.upper()

    def __str__(self) -> str:
        symbol = "Rs." if self.currency == "INR" else self.currency
        return f"{symbol} {self.amount:.2f}"

    def __repr__(self) -> str:
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    def __add__(self, other) -> "Money":
        if not isinstance(other, Money):
            raise TypeError("Can only add Money to another Money instance.")
        if self.currency != other.currency:
            raise ValueError(f"Cannot add different currencies: {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other) -> "Money":
        if not isinstance(other, Money):
            raise TypeError("Can only subtract Money from another Money instance.")
        if self.currency != other.currency:
            raise ValueError("Currencies must match for subtraction.")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor: float) -> "Money":
        if not isinstance(factor, (int, float)):
            raise TypeError("Can only multiply Money by an integer or float.")
        return Money(self.amount * factor, self.currency)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other) -> bool:
        if not isinstance(other, Money) or self.currency != other.currency:
            raise TypeError("Cannot compare incompatible Money instances.")
        return self.amount < other.amount

    def __gt__(self, other) -> bool:
        if not isinstance(other, Money) or self.currency != other.currency:
            raise TypeError("Cannot compare incompatible Money instances.")
        return self.amount > other.amount


class Cart:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.items: list[str] = []

    def add_item(self, item_name: str) -> None:
        self.items.append(item_name)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> str:
        return self.items[index]

    def __contains__(self, item_name: str) -> bool:
        return item_name in self.items

    def __add__(self, other: "Cart") -> "Cart":
        if not isinstance(other, Cart):
            raise TypeError("Can only merge another Cart.")
        merged_cart = Cart(owner=f"{self.owner} & {other.owner}")
        merged_cart.items = self.items + other.items
        return merged_cart

    def __str__(self) -> str:
        items_str = ", ".join(self.items) if self.items else "Empty"
        return f"Cart of {self.owner} ({len(self.items)} items): [{items_str}]"


def main() -> None:
    wallet = Money(500.0, "INR")
    salary = Money(1500.0, "INR")
    print(f"print(wallet) -> {wallet}")
    print(f"repr(wallet)  -> {repr(wallet)}")

    total = wallet + salary
    print(f"{wallet} + {salary} = {total}")

    expense = Money(300.0, "INR")
    balance = wallet - expense
    print(f"{wallet} - {expense} = {balance}")

    doubled = wallet * 2
    print(f"{wallet} * 2 = {doubled}")

    m1 = Money(500, "INR")
    m2 = Money(500, "INR")
    m3 = Money(800, "INR")

    print(f"m1 ({m1}) == m2 ({m2}) -> {m1 == m2}")
    print(f"m3 ({m3}) > m1 ({m1})  -> {m3 > m1}")
    print(f"m1 ({m1}) < m3 ({m3})  -> {m1 < m3}")

    cart1 = Cart("Tarun")
    cart1.add_item("Mechanical Keyboard")
    cart1.add_item("Wireless Mouse")

    cart2 = Cart("Ashmita")
    cart2.add_item("Laptop Stand")
    cart2.add_item("USB-C Hub")

    print(cart1)
    print(cart2)

    print(f"Number of items in Tarun's cart: len(cart1) = {len(cart1)}")
    print(f"First item in Tarun's cart: cart1[0] = '{cart1[0]}'")
    print(f"Second item in Tarun's cart: cart1[1] = '{cart1[1]}'")
    print(f"Is 'Wireless Mouse' in cart1? -> {'Wireless Mouse' in cart1}")
    print(f"Is 'Monitor' in cart1?        -> {'Monitor' in cart1}")

    combined = cart1 + cart2
    print(f"Combined Carts (cart1 + cart2): {combined}")
    print(f"Total items in combined cart: {len(combined)}")


if __name__ == "__main__":
    main()


# Output

# print(wallet) -> Rs. 500.00
# repr(wallet)  -> Money(amount=500.0, currency='INR')
# Rs. 500.00 + Rs. 1500.00 = Rs. 2000.00
# Rs. 500.00 - Rs. 300.00 = Rs. 200.00
# Rs. 500.00 * 2 = Rs. 1000.00
# m1 (Rs. 500.00) == m2 (Rs. 500.00) -> True
# m3 (Rs. 800.00) > m1 (Rs. 500.00)  -> True
# m1 (Rs. 500.00) < m3 (Rs. 800.00)  -> True
# Cart of Tarun (2 items): [Mechanical Keyboard, Wireless Mouse]
# Cart of Ashmita (2 items): [Laptop Stand, USB-C Hub]
# Number of items in Tarun's cart: len(cart1) = 2
# First item in Tarun's cart: cart1[0] = 'Mechanical Keyboard'
# Second item in Tarun's cart: cart1[1] = 'Wireless Mouse'
# Is 'Wireless Mouse' in cart1? -> True
# Is 'Monitor' in cart1?        -> False
# Combined Carts (cart1 + cart2): Cart of Tarun & Ashmita (4 items): [Mechanical Keyboard,Wireless Mouse, Laptop Stand, USB-C Hub]
# Total items in combined cart: 4