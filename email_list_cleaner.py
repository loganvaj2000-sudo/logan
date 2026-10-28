import csv
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
SOURCE_FILENAME = "prospects.csv"
CLEAN_FILENAME = "prospects_clean.csv"


def display_title():
    print("Welcome to the Email List Cleaner")
    print()


def read_prospects(filename):
    with open(FOLDER / filename, newline="") as file:
        reader = csv.reader(file)
        return [row for row in reader if row]


def clean_prospect(row):
    first_name, last_name, email = [value.strip() for value in row[:3]]
    return [first_name.title(), last_name.title(), email.lower()]


def write_prospects(filename, prospects):
    with open(FOLDER / filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(prospects)


def main():
    display_title()
    print(f"Source list: {SOURCE_FILENAME}")
    print(f"Cleaned list: {CLEAN_FILENAME}")
    print()

    rows = read_prospects(SOURCE_FILENAME)
    header, prospects = rows[0], rows[1:]
    cleaned = [header] + [clean_prospect(row) for row in prospects]
    write_prospects(CLEAN_FILENAME, cleaned)

    print("Congratulations! Your list has been cleaned!")


if __name__ == "__main__":
    main()
