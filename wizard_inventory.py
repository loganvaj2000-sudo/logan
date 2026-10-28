# Logan Vang
# 10/27/2026
# Wizard Inventory

import random
from pathlib import Path

DATA_FOLDER = Path(__file__).resolve().parent
ALL_ITEMS_FILE = DATA_FOLDER / "wizard_all_items.txt"
INVENTORY_FILE = DATA_FOLDER / "wizard_inventory.txt"
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


def read_file(filename):
    items = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                items.append(line)
    return items


def write_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        for item in inventory:
            file.write(f"{item}\n")


def walk(all_items, inventory):
    choices = [item for item in all_items if item not in inventory]
    if len(choices) == 0:
        print("While walking down a path, you find nothing new.")
        print()
        return

    item = random.choice(choices)
    print(f"While walking down a path, you see {item}.")
    grab = input("Do you want to grab it? (y/n): ").lower()
    if grab == "y":
        if len(inventory) >= MAX_ITEMS:
            print("You can't carry any more items. Drop something first.")
        else:
            inventory.append(item)
            write_inventory(inventory)
            print(f"You picked up {item}.")
    print()


def show(inventory):
    if len(inventory) == 0:
        print("You aren't carrying any items.")
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
    print()


def drop(inventory):
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
        all_items = read_file(ALL_ITEMS_FILE)
    except FileNotFoundError:
        print(f"Could not find {ALL_ITEMS_FILE.name}.")
        print("Exiting program. Bye!")
        return

    try:
        inventory = read_file(INVENTORY_FILE)
    except FileNotFoundError:
        inventory = []
        write_inventory(inventory)

    display_menu()
    while True:
        command = input("Command: ").lower()
        if command == "walk":
            walk(all_items, inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop(inventory)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            print()


if __name__ == "__main__":
    main()
