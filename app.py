from users.admin import Admin
from users.visitor import Visitor
from inventory.inventory import Inventory
from inventory.item import Item

def main():
    inventory = Inventory()
    admin = Admin("Admin")
    visitor = Visitor("Visitor")
    current_user = None

    initial_items = [
        Item("Laptop", "A powerful laptop", 1200.0, 10),
        Item("Mouse", "An ergonomic mouse", 20.0, 50),
        Item("Keyboard", "A mechanical keyboard", 100.0, 20)
    ]
    for item in initial_items:
        inventory.add_item(item)

    print("Welcome to the Store Inventory Management System!")

    while True:
        if current_user is None:
            print("\nLogin Menu:")
            print("1. Login as Admin")
            print("2. Login as Visitor")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                current_user = admin
            elif choice == '2':
                current_user = visitor
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

        else:
            if isinstance(current_user, Admin):
                print("\nAdmin Menu:")
                print("1. Add item to inventory")
                print("2. View inventory")
                print("3. Logout")
                choice = input("Enter your choice (1-3): ")

                if choice == '1':
                    admin.add_item_to_inventory(inventory)
                elif choice == '2':
                    admin.view_inventory(inventory)
                elif choice == '3':
                    current_user = None
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

            elif isinstance(current_user, Visitor):
                print("\nVisitor Menu:")
                print("1. View inventory")
                print("2. Purchase item")
                print("3. Logout")
                choice = input("Enter your choice (1-3): ")

                if choice == '1':
                    visitor.view_inventory(inventory)
                elif choice == '2':
                    visitor.purchase_item(inventory)
                elif choice == '3':
                    current_user = None
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    print("Thank you for using the Store Inventory Management System!")

if __name__ == "__main__":
    main()
