# Part 2

#     Create a file called menu_editor.py , which will have the following functions:
#         show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to :
#             View an Item (V)
#             Add an Item (A)
#             Delete an Item (D)
#             Update an Item (U)
#             Show the Menu (S)
#             Call the appropriate function that matches the user’s input.


#     When the user chooses to exit the program, display the restaurant menu and exit the program.


from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    """this function should display the program menu (not the restaurant menu!)"""
    while True:
        print("\n--- Restaurant Menu Management ---")
        print("View an Item (V)")
        print("Add an Item (A)")
        print("Delete an Item (D)")
        print("Update an Item (U)")
        print("Show the Menu (S)")
        print("Exit (E)")

        choice = input("choose an option: ").strip().upper()

        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("exiting the program")
            show_restaurant_menu()  # Display menu before exiting
            break
        else:
            print("invalid choice, try again")


def view_item():
    """shows a specific item by its name"""
    name = input("enter the name of the item you want to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"item found: ID {item.item_id}, name {item.name}, price {item.price:.2f}")
    else:
        print("item not found.")


#         add_item_to_menu() - this function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
#             If the item was added successfully print a message which states: item was added successfully.
def add_item_to_menu():
    """adds a new item to the menu"""
    name = input("enter item name: ")
    price = float(input("enter item price: "))
    item = MenuItem(name, price)
    
    try:
        item.save()  # save the item to the database
        print("Item was added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")


#         remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
#             If the item was deleted successfully – print a message to let the user know this was completed.
#             If not – print a message which states that there was an error.
def remove_item_from_menu():
    """removes item from the menu by its name"""
    name = input("enter the name of the to remove: ")
    item = MenuManager.get_by_name(name)
    
    if item:
        try:
            item.delete()  # Delete the item from the database
            print(f"item '{name}' was deleted successfully")
        except Exception as e:
            print(f"error deleting item: {e}")
    else:
        print("item not found")


#         update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
#             If the item was updated successfully – print a message to let the user know this was completed.
#             If not – print a message which states that there was an error.
def update_item_from_menu():
    """update an existing item name and price"""
    name = input("enter the name of the item you want to update: ")
    item = MenuManager.get_by_name(name)
    
    if item:
        new_name = input("enter the new name for the item: ")
        new_price = float(input("enter the new price for the item: "))
        
        try:
            item.update(new_name, new_price)  # Update the item's details
            print(f"item '{name}' was updated successfully")
        except Exception as e:
            print(f"error updating item: {e}")
    else:
        print("item not found")


#         show_restaurant_menu() - print the restaurant’s menu.
def show_restaurant_menu():
    """shows all items in the restaurant menu"""
    items = MenuManager.all_items()
    if items:
        print("\n--- Restaurant Menu ---")
        for item in items:
            print(f"ID: {item.item_id}, name: {item.name}, price: {item.price:.2f}")
    else:
        print("the menu is currently empty")


show_user_menu() # i made a mistake and fetched the items by ID (instead of item name) originally in menu_item.py, the program works and i need to sleep