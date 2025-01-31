#!/usr/bin/python3
"""Square class with a private instance attribute"""


class Square:
    """Square class with a private instance attribute: size"""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type/value verification)
        """
        self.__size = size
