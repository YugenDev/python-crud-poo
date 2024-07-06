from users.user import User
from inventory.inventory import Inventory
from inventory.item import Item

class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def add_item_to_inventory(self, inventory):
        name = input("Enter item name: ")
        description = input("Enter item description: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        item = Item(name, description, price, quantity)
        inventory.add_item(item)
        print(f"{name} has been added to the inventory.")

    def view_inventory(self, inventory):
        print("\nCurrent Inventory:")
        print(inventory.display_inventory())
