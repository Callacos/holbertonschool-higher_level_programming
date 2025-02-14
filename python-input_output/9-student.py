#!/usr/bin/python3
""" Module définissant la classe Student avec des méthodes
pour la sérialisation JSON.
"""


class Student:

    """ Classe qui définit un étudiant par :
    - Prénom
    - Nom
    - Âge
    """
    def __init__(self, first_name, last_name, age):
        """ Initialise une nouvelle instance de la classe Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
