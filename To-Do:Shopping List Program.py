print("Welcome to the To-Do/Shopping List program!")
def add_item():
    new_item = input("Enter the item to add to the list: ")
    file = open("shopping.txt", "a")
    new_item = new_item + "\n"
    file.write(new_item)
    file.close()
    

def output_items():
    try:
        file = open("shopping.txt", "r")
    except FileNotFoundError:
        file = open("shopping.txt", "w")
        file.close()
    else:
        print("-----------------------------")
        for item in file:
            item = item.strip()
            print(item)
        file.close()
        print("-----------------------------")


def sort_items():
    try:
        file = open("shopping.txt", "r")
    except FileNotFoundError:
        file = open("shopping.txt", "w")
        file.close()
    else:
        item_list = []
        for item in file:
            item = item.strip()
            item_list.append(item)
        file.close()
        item_list.sort()
        file = open("shopping.txt", "w")
        for item in item_list:
            item = item + "\n"
            file.write(item)
        file.close()
    