#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique."""

    @abstractmethod
    def area(self):
        """Calcule l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule le périmètre de la forme."""
        pass


class Circle(Shape):
    """Classe représentant un cercle."""

    def __init__(self, radius):
        """Initialise un cercle avec un rayon donné."""
        self.radius = radius

    def area(self):
        """Calcule l'aire du cercle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcule le périmètre du cercle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe représentant un rectangle."""

    def __init__(self, width, height):
        """Initialise un rectangle avec une largeur et une hauteur données."""
        self.width = width
        self.height = height

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Test avec un cercle et un rectangle
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Cercle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)
