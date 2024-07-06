from users.user import User
from inventory.inventory import Inventory

class Visitor(User):
    def __init__(self, name):
        super().__init__(name)

    def view_inventory(self, inventory):
        print("\nCurrent Inventory:")
        print(inventory.display_inventory())

    def purchase_item(self, inventory):
        name = input("Enter item name to purchase: ")
        item = inventory.find_item(name)
        if item:
            item.quantity -= 1
            print(f"You have purchased {name}.")
        else:
            print(f"{name} not found in inventory.")
