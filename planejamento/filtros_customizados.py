from django import template


def replace_decimal_separator(value):
    return str(value).replace(',', '.')

