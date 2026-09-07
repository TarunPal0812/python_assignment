# 9. Dictionary-Based Inventory 
# Create: 
# inventory = { 
# "laptop": 10, 
# "mouse": 50, 
# "keyboard": 25 
# } 
# Implement: 
# add_product() 
# remove_product() 
# sell_product() 
# restock_product() 
# check_stock() 
# Rules 
# ● Product cannot have negative stock 
# ● Cannot sell more than available stock 
# ● Cannot restock a nonexistent product 
# ● Cannot sell a nonexistent product 
# Use custom exceptions. 

from inventory import add_product, sell_product,restock_product,check_stock,remove_product
from custom_exception import ProductNotFoundError,NegativeStockError,InsufficientStockError

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 25
}

def main() -> None:
    """
    Run the inventory management program.
    """

    try:
       
        add_product(inventory, "monitor", 15)

        sell_product(inventory, "laptop", 2)

        restock_product(inventory, "mouse", 10)

        print("Laptop Stock:", check_stock(inventory, "laptop"))
        print("Mouse Stock:", check_stock(inventory, "mouse"))
        print("Monitor Stock:", check_stock(inventory, "monitor"))

        remove_product(inventory, "keyboard")

        print("Inventory:", inventory)

    except (
        ProductNotFoundError,
        NegativeStockError,
        InsufficientStockError
    ) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()


# Output

# Laptop Stock: 8
# Mouse Stock: 60
# Monitor Stock: 15
# Inventory: {'laptop': 8, 'mouse': 60, 'monitor': 15}