import datetime

print("Welcome to the To-Do/Shopping List program!")

def add_item():
    new_item = input("Enter the item to add to the list: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("shopping.txt", "a") as file:
        file.write(f"{current_time} - {new_item}\n")

def output_items():
    try:
        with open("shopping.txt", "r") as file:
            print("-----------------------------")
            for item in file:
                print(item.strip())
            print("-----------------------------")
            print("Time is written in GMT")
    except FileNotFoundError:
        with open("shopping.txt", "w") as file:
            pass  # Create an empty file if it doesn't exist

def sort_items_alphabetically():
    try:
        with open("shopping.txt", "r") as file:
            item_list = [line.strip() for line in file]
        item_list.sort(key=lambda x: x.split(" - ")[1])
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
        item_list.sort(key=lambda x: datetime.datetime.strptime(x.split(" - ")[0], "%Y-%m-%d %H:%M:%S"), reverse=True)
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

while True:
    print("\nWhat would you like to do?")
    print("1. Add an item")
    print("2. Output the list")
    print("3. Sort the list alphabetically")
    print("4. Sort the list by date")
    print("5. Tick off an item")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        output_items()
    elif choice == "3":
        sort_items_alphabetically()
    elif choice == "4":
        sort_items_by_date()
    elif choice == "5":
        tick_item()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
