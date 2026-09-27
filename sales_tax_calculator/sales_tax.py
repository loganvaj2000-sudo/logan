#!/usr/bin/env python3
# Logan Vaj
# 2026-09-27
# Sales Tax Calculator

TAX_RATE = 0.06


def calculate_tax(total):
    return round(total * TAX_RATE, 2)


def calculate_total_after_tax(total):
    return round(total + calculate_tax(total), 2)
