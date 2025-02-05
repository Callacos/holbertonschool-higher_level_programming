#!/usr/bin/python3
""" Module that contains the BaseGeometry class with area and
integer_validator methods """


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
