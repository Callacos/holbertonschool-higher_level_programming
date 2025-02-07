#!/usr/bin/python3
class Fish:
    """Classe représentant un poisson."""

    def swim(self):
        """Méthode pour nager."""
        print("Le poisson nage.")

    def habitat(self):
        """Méthode pour décrire l'habitat."""
        print("Le poisson vit dans l'eau.")


class Bird:
    """Classe représentant un oiseau."""

    def fly(self):
        """Méthode pour voler."""
        print("L'oiseau vole.")

    def habitat(self):
        """Méthode pour décrire l'habitat."""
        print("L'oiseau vit dans le ciel.")


class FlyingFish(Fish, Bird):
    """Classe représentant un poisson volant."""

    def fly(self):
        """Méthode surchargée pour voler."""
        print("Le poisson volant plane !")

    def swim(self):
        """Méthode surchargée pour nager."""
        print("Le poisson volant nage !")

    def habitat(self):
        """Méthode surchargée pour décrire l'habitat."""
        print("Le poisson volant vit à la fois dans l'eau et dans le ciel !")


# Test de la classe FlyingFish
if __name__ == "__main__":
    flying_fish = FlyingFish()

    print("Méthodes du poisson volant :")
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    print("\nOrdre de résolution des méthodes :")
    print(FlyingFish.mro())
