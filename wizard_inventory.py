MAX_ITEMS = 4


def display_title():
    print("The Wizard Inventory program")
    print()


def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def show(inventory):
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}")
    print()


def grab(inventory):
    if len(inventory) >= MAX_ITEMS:
        print("You can't carry any more items. Drop something first.")
    else:
        item = input("Name: ")
        inventory.append(item)
        print(f"{item} was added.")
    print()


def get_item_number(inventory):
    try:
        number = int(input("Number: "))
    except ValueError:
        print("Invalid item number.")
        return None
    if number < 1 or number > len(inventory):
        print("Invalid item number.")
        return None
    return number


def edit(inventory):
    number = get_item_number(inventory)
    if number is not None:
        print()
        inventory[number - 1] = input("Updated name: ")
        print(f"Item number {number} was updated.")
    print()


def drop(inventory):
    number = get_item_number(inventory)
    if number is not None:
        item = inventory.pop(number - 1)
        print(f"{item} was dropped.")
    print()


def main():
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    commands = {"show": show, "grab": grab, "edit": edit, "drop": drop}

    display_title()
    display_menu()
    while True:
        command = input("Command: ").strip().lower()
        if command == "exit":
            print("Bye!")
            break
        elif command in commands:
            commands[command](inventory)
        else:
            print("Not a valid command. Please try again.")
            print()


if __name__ == "__main__":
    main()
