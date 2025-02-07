#!/usr/bin/python3
class CountedIterator:
    """Un itérateur qui compte le nombre d'éléments parcourus."""

    def __init__(self, iterable):
        """Initialise l'itérateur compté avec un itérable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Retourne l'objet lui-même comme itérateur."""
        return self

    def __next__(self):
        """Retourne le prochain élément et incrémente le compteur."""
        self.count += 1
        return next(self.iterator)

    def get_count(self):
        """Retourne le nombre d'éléments parcourus."""
        return self.count


# Test de la classe CountedIterator
if __name__ == "__main__":
    # Création d'un CountedIterator avec une liste
    counted_iter = CountedIterator([1, 2, 3, 4, 5])

    # Itération sur les éléments
    for item in counted_iter:
        print(f"Élément: {item}, Compteur: {counted_iter.get_count()}")

    # Vérification du compteur final
    print(f"Nombre total d'éléments parcourus: {counted_iter.get_count()}")

    # Test avec un appel manuel à __next__
    counted_iter2 = CountedIterator("abc")
    print(next(counted_iter2))
    print(next(counted_iter2))
    print(f"Compteur après 2 appels manuels: {counted_iter2.get_count()}")
