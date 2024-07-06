from inventory.item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_inventory(self):
        if not self.items:
            return "Inventory is empty."
        else:
            return "\n".join(item.display_info() for item in self.items)

    def find_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
