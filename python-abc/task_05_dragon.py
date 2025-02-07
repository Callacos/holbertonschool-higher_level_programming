#!/usr/bin/python3
class SwimMixin:
    """Mixin fournissant la capacité de nager."""

    def swim(self):
        """Méthode pour nager."""
        print("La créature nage !")


class FlyMixin:
    """Mixin fournissant la capacité de voler."""

    def fly(self):
        """Méthode pour voler."""
        print("La créature vole !")


class Dragon(SwimMixin, FlyMixin):
    """Classe représentant un dragon avec des capacités de nage et de vol."""

    def roar(self):
        """Méthode spécifique au dragon pour rugir."""
        print("Le dragon rugit !")


# Test de la classe Dragon
if __name__ == "__main__":
    draco = Dragon()

    print("Capacités du dragon :")
    draco.swim()
    draco.fly()
    draco.roar()

    print("\nMéthodes héritées du dragon :")
    print(", ".join(method for method in dir(draco) if not method.startswith("__")))
