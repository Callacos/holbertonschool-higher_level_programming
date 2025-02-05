#!/usr/bin/python3
""" Module that contains the Square class that inherits from Rectangle """


class BaseGeometry:
    """ Classe de base pour la géométrie """

    def area(self):
        """ Méthode qui soulève une exception avec un message
        indiquant que la méthode n'est pas implémentée. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Valide que value est un entier positif, sinon
          lève une exception. """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Classe Rectangle qui hérite de BaseGeometry """

    def __init__(self, width, height):
        """ Initialisation avec width et height. Ils doivent
          être des entiers positifs. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Implémentation de la méthode area() pour
          calculer l'aire du rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Méthode __str__ pour retourner la description du rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """ Méthode __repr__ pour retourner une représentation du rectangle
        (utile pour les tests ou l'interprétation) """
        return self.__str__()


class Square(Rectangle):
    """ Classe Square qui hérite de Rectangle """

    def __init__(self, size):
        """ Initialisation avec size. La taille doit être validée
        comme un entier positif. """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Implémentation de la méthode area() pour
          calculer l'aire du carré """
        return self.__size * self.__size

    def __str__(self):
        """ Méthode __str__ pour retourner la description du carré """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """ Méthode __repr__ pour retourner une représentation du carré
        (utile pour les tests ou l'interprétation) """
        return self.__str__()
