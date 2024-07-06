class Item:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"{self.name} - {self.description} - ${self.price} - Quantity: {self.quantity}"
