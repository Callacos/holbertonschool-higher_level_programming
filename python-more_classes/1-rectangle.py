#!/usr/bin/python3
"""Module définissant une classe Rectangle"""


class Rectangle:
    """Classe définissant un rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle. Par défaut 0.
            height (int): La hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): La nouvelle largeur.

        Raises:
            TypeError: Si la largeur n'est pas un entier.
            ValueError: Si la largeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.

        Args:
            value (int): La nouvelle hauteur.

        Raises:
            TypeError: Si la hauteur n'est pas un entier.
            ValueError: Si la hauteur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
