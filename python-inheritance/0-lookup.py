#!/usr/bin/python3
""" Module that contains a function that returns the
 list of available attributes and methods of an object """


def lookup(obj):
    """ Retourne la liste des attributs et méthodes disponibles d'un objet. """
    return dir(obj)