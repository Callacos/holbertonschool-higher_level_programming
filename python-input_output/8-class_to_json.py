#!/usr/bin/python3
""" Module qui contient une fonction qui renvoie la description du
dictionnaire avec une structure de données simple pour la sérialisation
JSON d'un objet.
"""


def class_to_json(obj):

    return obj.__dict__
