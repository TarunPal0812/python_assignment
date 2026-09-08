from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    def __init__(self, provider_name: str) -> None:
        self.provider_name = provider_name

    @abstractmethod
    def authenticate(self) -> bool:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

    def print_receipt(self, transaction_id: str, amount: float) -> None:
        print("-" * 40)
        print(f"[{self.provider_name}] PAYMENT RECEIPT")
        print(f"Transaction ID : {transaction_id}")
        print(f"Amount Paid    : Rs. {amount:.2f}")
        print("Status         : SUCCESS")
        print("-" * 40)


class UPIPayment(PaymentGateway):
    def __init__(self, upi_id: str) -> None:
        super().__init__(provider_name="UPI")
        self.upi_id = upi_id

    def authenticate(self) -> bool:
        if "@" in self.upi_id:
            print(f"UPI ID '{self.upi_id}' verified via PIN.")
            return True
        print(f"Invalid UPI ID: '{self.upi_id}'")
        return False

    def pay(self, amount: float) -> bool:
        if not self.authenticate():
            print("Payment failed: Authentication error.")
            return False

        print(f"Deducting Rs. {amount:.2f} from bank account linked to {self.upi_id}...")
        self.print_receipt(transaction_id="UPI-982341", amount=amount)
        return True


class CreditCardPayment(PaymentGateway):
    def __init__(self, card_number: str, card_holder: str) -> None:
        super().__init__(provider_name="Credit Card Gateway")
        self.card_number = card_number
        self.card_holder = card_holder

    def authenticate(self) -> bool:
        if len(self.card_number.replace(" ", "")) == 16:
            print(f"Card ending in {self.card_number[-4:]} authorized via OTP.")
            return True
        print("Card authentication failed: Invalid card number.")
        return False

    def pay(self, amount: float) -> bool:
        if not self.authenticate():
            print("Payment failed: Authentication error.")
            return False

        print(f"Charging Rs. {amount:.2f} to card of {self.card_holder}...")
        self.print_receipt(transaction_id="CC-554129", amount=amount)
        return True


def checkout(gateway: PaymentGateway, amount: float) -> None:
    print(f"\nProcessing checkout with {gateway.provider_name}...")
    gateway.pay(amount)


def main() -> None:

    upi = UPIPayment(upi_id="tarun@oksbi")
    checkout(upi, 1250.00)

    card = CreditCardPayment(card_number="4111 2222 3333 4444", card_holder="Tarun Pal")
    checkout(card, 4999.50)


if __name__ == "__main__":
    main()


# Output

# Processing checkout with UPI...
# UPI ID 'tarun@oksbi' verified via PIN.
# Deducting Rs. 1250.00 from bank account linked to tarun@oksbi...
# ----------------------------------------
# [UPI] PAYMENT RECEIPT
# Transaction ID : UPI-982341
# Amount Paid    : Rs. 1250.00
# Status         : SUCCESS
# ----------------------------------------

# Processing checkout with Credit Card Gateway...
# Card ending in 4444 authorized via OTP.
# Charging Rs. 4999.50 to card of Tarun Pal...
# ----------------------------------------
# [Credit Card Gateway] PAYMENT RECEIPT
# Transaction ID : CC-554129
# Amount Paid    : Rs. 4999.50
# Status         : SUCCESS
# ----------------------------------------