#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"


# Demonstration of usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(dog.sound())  # Output: Bark
    print(cat.sound())  # Output: Meow
