#!/usr/bin/python3

class Circle:
    """Classe représentant un cercle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calcule et retourne l'aire du cercle."""
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        """Calcule et retourne le périmètre du cercle."""
        return 2 * 3.14 * self.radius


class Rectangle:
    """Classe représentant un rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche les informations d'une forme géométrique.

    Args:
        shape: Objet représentant la forme géométrique
    """
    print(f"Aire: {shape.area()}")
    print(f"Périmètre: {shape.perimeter()}")


# Script demonstrating the use of duck typing with geometric shapes
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

# Call shape_info to display information about the circle
shape_info(circle)

# Call shape_info to display information about the rectangle
shape_info(rectangle)
