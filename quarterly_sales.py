QUARTERS = 4


def display_title():
    print("The Quarterly Sales program")
    print()


def get_sales():
    sales = []
    for quarter in range(1, QUARTERS + 1):
        while True:
            try:
                amount = float(input(f"Enter sales for Q{quarter}: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            if amount < 0:
                print("Sales can't be negative. Please try again.")
                continue
            sales.append(round(amount, 2))
            break
    print()
    return sales


def display_results(sales):
    total = round(sum(sales), 2)
    average = round(total / len(sales), 2)
    print(f"Total: {total:.2f}")
    print(f"Average Quarter: {average:.2f}")
    print(f"Lowest Quarter: {min(sales):.2f}")
    print(f"Highest Quarter: {max(sales):.2f}")


def main():
    display_title()
    sales = get_sales()
    display_results(sales)


if __name__ == "__main__":
    main()
