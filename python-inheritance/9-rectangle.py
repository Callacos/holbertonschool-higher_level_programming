#!/usr/bin/python3
""" Module that contains the Rectangle class that inherits from
BaseGeometry """


class BaseGeometry:
    """ Classe BaseGeometry """

    def area(self):
        """ Méthode qui soulève une exception avec un message
        indiquant que l'area() n'est pas implémentée. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Valide que value est un entier positif, sinon lève une
        exception. """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Classe Rectangle qui hérite de BaseGeometry """

    def __init__(self, width, height):
        """ Initialisation avec width et height. Ils doivent être des
        entiers positifs. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Implémentation de la méthode area() pour calculer l'aire du
        rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Méthode __str__ pour retourner la description du rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """ Méthode __repr__ pour retourner une représentation du rectangle
        (utile pour les tests ou l'interprétation) """
        return self.__str__()
