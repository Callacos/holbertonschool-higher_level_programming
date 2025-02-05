#!/usr/bin/python3
""" Module that contains a function to check if an object is an
instance of a specified class or a class that inherited from it """


def is_kind_of_class(obj, a_class):
    """ Retourne True si obj est une instance de a_class ou
    d'une classe qui en hérite, sinon False. """
    return isinstance(obj, a_class)
