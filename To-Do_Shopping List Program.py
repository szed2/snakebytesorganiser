import datetime

print("Welcome to the To-Do/Shopping List program!")


def add_item():
    new_item = input("Enter the item to add to the list: ")
    due_date = input("Enter the due date (YYYY-MM-DD format): ")

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("shopping.txt", "a") as file:
        file.write(f"{current_time} - {due_date} - {new_item}\n")


def output_items():
    try:
        with open("shopping.txt", "r") as file:
            print("-----------------------------")
            for item in file:
                print(item.strip())
            print("-----------------------------")
            print("Time is written in GMT if run on Trinket/Time is written in GMT+8 if run on VSCode2")
    except FileNotFoundError:
        with open("shopping.txt", "w") as file:
            pass  # Create an empty file if it doesn't exist


def sort_items_alphabetically():
    try:
        with open("shopping.txt", "r") as file:
            item_list = [line.strip() for line in file]
            item_list.sort(key=lambda x: x.split(" - ")[2])  # Sort by item name
        with open("shopping.txt", "w") as file:
            for item in item_list:
                file.write(item + "\n")
    except FileNotFoundError:
        with open("shopping.txt", "w") as file:
            pass  # Create an empty file if it doesn't exist


def sort_items_by_date():
    try:
        with open("shopping.txt", "r") as file:
            item_list = [line.strip() for line in file]
            # Sort by due date (formatted as YYYY-MM-DD)
            item_list.sort(key=lambda x: datetime.datetime.strptime(x.split(" - ")[1], "%Y-%m-%D"))
        with open("shopping.txt", "w") as file:
            for item in item_list:
                file.write(item + "\n")
    except FileNotFoundError:
        with open("shopping.txt", "w") as file:
            pass  # Create an empty file if it doesn't exist


def tick_item():
    item_to_tick = input("Enter the item to tick off: ")
    with open("shopping.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip() != item_to_tick:
                file.write(line)
        file.truncate()
        print(f"Item '{item_to_tick}' ticked off.")


def add_due_date():
    """
    This function allows the user to add a due date to an existing item.
    """
    item_name = input("Enter the name of the item to add a due date to: ")
    due_date = input("Enter the due date (YYYY-MM-DD format): ")

    # Read the existing list
    try:
        with open("shopping.txt", "r") as file:
            item_list = file.readlines()
    except FileNotFoundError:
        print("No items found in the list.")
        return

    # Update the item with due date
    updated_list = []
    for item in item_list:
        if item.strip().split(" - ")[2] == item_name:  # Check for item name
            updated_item = f"{item.strip().split(' - ')[0]} - {due_date} - {item_name.strip()}\n"
            updated_list.append(updated_item)
        else:
            updated_list.append(item)

    # Write the updated list to the file
    with open("shopping.txt", "w") as file:
        file.writelines(updated_list)
    print(f"Due date added to '{item_name}'.")


while True:
    print("\nWhat would you like to do?")
    print("1. Add an item")
    print("2. Output the list")
    print("3. Sort the list alphabetically")
