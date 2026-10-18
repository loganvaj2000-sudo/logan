# Logan
# September 27, 2026
# Sales Tax Calculator

TAX_RATE = 0.06


def calculate_tax(total):
    return round(total * TAX_RATE, 2)


def get_items_total():
    print("ENTER ITEMS (ENTER 0 TO END)")
    total = 0.0
    while True:
        cost = float(input("Cost of item: "))
        if cost == 0:
            break
        total += cost
    return round(total, 2)


def main():
    print("Sales Tax Calculator")
    print()

    again = "y"
    while again.lower() == "y":
        total = get_items_total()
        sales_tax = calculate_tax(total)
        total_after_tax = round(total + sales_tax, 2)

        print("Total:", total)
        print("Sales tax:", sales_tax)
        print("Total after tax:", total_after_tax)
        print()

        again = input("Again? (y/n): ")
        print()

    print("Thanks, bye!")


if __name__ == "__main__":
    main()
