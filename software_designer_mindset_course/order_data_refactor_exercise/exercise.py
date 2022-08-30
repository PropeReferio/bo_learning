from dataclasses import dataclass
from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class LineItem():
    name: str
    quantity: int
    price: int

    @property
    def line_price(self) -> int:
        return self.quantity * self.price


class Order:
    def __init__(self):
        self.line_items: list[LineItem] = []
        self.status: str = "open"

    def add_item(self, item: LineItem) -> None:
        self.line_items.append(item)

    @property
    def total_price(self) -> int:
        return sum([item.line_price for item in self.line_items])


def main() -> None:
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
