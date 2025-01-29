#!/usr/bin/python3
"""Module contenant la définition de la classe Square."""


class Square:
    """Représente un carré.

    Attributs privés :
        __size (int) : La taille du côté du carré (doit être un entier >= 0).

    Méthodes publiques :
        area() : Retourne l'aire actuelle du carré.
    """

    def __init__(self, size=0):
        """Initialise une instance de la classe Square.

        Args:
            size (int, optionnel) : La taille du côté du carré (par défaut 0).

        Raises:
            TypeError : Si size n'est pas un entier.
            ValueError : Si size est inférieur à 0.
        """
        self.size = size

    @property
    def size(self):
        """Récupère la taille du côté du carré.

        Returns:
            int : La taille actuelle du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du côté du carré.

        Args:
            value (int) : La nouvelle taille à attribuer au carré.

        Raises:
            TypeError : Si value n'est pas un entier.
            ValueError : Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et retourne l'aire actuelle du carré.

        Returns:
            int : L'aire du carré (size ** 2).
        """
        return self.__size ** 2
