#!/usr/bin/python3
""" Module that contains the BaseGeometry class with an area method """


class BaseGeometry:
    """ Classe BaseGeometry """

    def area(self):
        """ Méthode qui soulève une exception avec un message 
        indiquant que l'area() n'est pas implémentée. """
        raise Exception("area() is not implemented")
