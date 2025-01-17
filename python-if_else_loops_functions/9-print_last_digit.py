#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number.

    Args:
        number: The input number
    Returns:
        The last digit of the number
    """
    number = abs(number)
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit
