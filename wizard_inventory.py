import random
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
ALL_ITEMS_FILENAME = FOLDER / "wizard_all_items.txt"
INVENTORY_FILENAME = FOLDER / "wizard_inventory.txt"
MAX_ITEMS = 4


def display_title():
    print("The Wizard Inventory program")
    print()


def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def read_items(filename):
    with open(filename) as file:
        return [line.strip() for line in file if line.strip()]


def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")


def walk(all_items, inventory):
    available_items = [item for item in all_items if item not in inventory]
    if not available_items:
        print("While walking down a path, you don't see anything.")
        print()
        return
    item = random.choice(available_items)
    print(f"While walking down a path, you see {item}.")
    choice = input("Do you want to grab it? (y/n): ").strip().lower()
    if choice == "y":
        if len(inventory) >= MAX_ITEMS:
            print("You can't carry any more items. Drop something first.")
        else:
            inventory.append(item)
            write_inventory(inventory)
            print(f"You picked up {item}.")
    print()


def show(all_items, inventory):
    if not inventory:
        print("You aren't carrying any items.")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}")
    print()


def drop(all_items, inventory):
    try:
        number = int(input("Number: "))
    except ValueError:
        print("Invalid item number.")
        print()
        return
    if number < 1 or number > len(inventory):
        print("Invalid item number.")
    else:
        item = inventory.pop(number - 1)
        write_inventory(inventory)
        print(f"You dropped {item}.")
    print()


def main():
    display_title()

    try:
        all_items = read_items(ALL_ITEMS_FILENAME)
    except FileNotFoundError:
        print(f"Could not find {ALL_ITEMS_FILENAME.name} file.")
        print("Exiting program. Bye!")
        return

    try:
        inventory = read_items(INVENTORY_FILENAME)
    except FileNotFoundError:
        print(f"Could not find {INVENTORY_FILENAME.name} file.")
        print("Wizard is starting with no inventory.")
        print()
        inventory = []
        write_inventory(inventory)

    commands = {"walk": walk, "show": show, "drop": drop}

    display_menu()
    while True:
        command = input("Command: ").strip().lower()
        if command == "exit":
            print("Bye!")
            break
        elif command in commands:
            commands[command](all_items, inventory)
        else:
            print("Not a valid command. Please try again.")
            print()


if __name__ == "__main__":
    main()
