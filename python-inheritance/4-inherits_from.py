#!/usr/bin/python3
""" Module that contains a function to check if an object is an
instance of a class that inherited (directly or indirectly) from
the specified class """


def inherits_from(obj, a_class):
    """ Retourne True si obj est une instance d'une classe qui hérite
    (directement ou indirectement) de a_class, sinon False. """
    return isinstance(obj, a_class) and type(obj) is not a_class
