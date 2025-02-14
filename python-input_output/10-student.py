#!/usr/bin/python3
""" Module defining the Student class with an enhanced
to_json method for selective attribute retrieval.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ Initializes a new instance of the Student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary representation of the Student instance.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
