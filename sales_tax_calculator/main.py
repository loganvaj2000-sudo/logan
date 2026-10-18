#!/usr/bin/env python3
# Logan Vaj
# 2026-09-27
# Sales Tax Calculator

import sales_tax


def get_items():
    print("ENTER ITEMS (ENTER 0 TO END)")
    total = 0
    while True:
        cost = float(input("Cost of item: "))
        if cost == 0:
            break
        total += cost
    return round(total, 2)


def display_results(total):
    tax = sales_tax.calculate_tax(total)
    total_after_tax = sales_tax.calculate_total_after_tax(total)
    print("Total:", total)
    print("Sales tax:", tax)
    print("Total after tax:", total_after_tax)


def main():
    print("Sales Tax Calculator")
    print()
    while True:
        total = get_items()
        display_results(total)
        again = input("Again? (y/n): ")
        print()
        if again.lower() != "y":
            break
    print("Thanks, bye!")


if __name__ == "__main__":
    main()
