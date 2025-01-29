#!/usr/bin/python3
""" This module contains an empty class Square that defines a square. """


class Square:
    """
    This is an empty class Square that defines a square.
    """

    def __init__(self, size=0):
        """
        The __init__ method of the class Square initializes the instance.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            None
        """

        self.__size = size

    def area(self):
        """
        The area method of the class Square returns the area of the square.

        Args:
            None

        Raises:
            None

        Returns:
            int: The area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """
        The size getter method of the class Square
        returns the size of the square.

        Args:
            None

        Raises:
            None

        Returns:
            int: The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        The size setter method of the class Square sets the size of the square.

        Args:
            value (int): The size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        The my_print method of the class Square prints the square.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """

        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
