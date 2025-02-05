#!/usr/bin/python3
""" Module that contains a function to check if an object is
exactly an instance of a specified class """


def is_same_class(obj, a_class):
    """ Retourne True si obj est exactement une instance de a_class,
    sinon False. """
    return type(obj) is a_class
