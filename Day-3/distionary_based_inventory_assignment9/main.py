from inventory import InventoryManager
from exceptions import (
    ProductNotFoundError,
    NegativeStockError,
    InsufficientStockError,
)


def main() -> None:
    initial_inventory = {
        "laptop": 10,
        "mouse": 50,
        "keyboard": 25,
    }

    manager = InventoryManager(initial_inventory)

    try:
        manager.add_product("monitor", 15)
        manager.sell_product("laptop", 2)
        manager.restock_product("mouse", 10)

        print("Laptop Stock:", manager.check_stock("laptop"))
        print("Mouse Stock:", manager.check_stock("mouse"))
        print("Monitor Stock:", manager.check_stock("monitor"))

        manager.remove_product("keyboard")
        print("Inventory:", manager.get_inventory())

    except (
        ProductNotFoundError,
        NegativeStockError,
        InsufficientStockError,
    ) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

# Output match Day-2:
# Laptop Stock: 8
# Mouse Stock: 60
# Monitor Stock: 15
# Inventory: {'laptop': 8, 'mouse': 60, 'monitor': 15}
