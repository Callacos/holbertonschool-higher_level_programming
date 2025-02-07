#!/usr/bin/python3
class VerboseList(list):
    """Une liste personnalisée qui affiche des notifications lors des modifications."""

    def append(self, item):
        """Ajoute un élément à la liste et affiche une notification."""
        super().append(item)
        print(f"Ajouté {item} à la liste.")

    def extend(self, iterable):
        """Étend la liste avec un itérable et affiche une notification."""
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print(f"Étendu la liste avec {items_added} élément(s).")

    def remove(self, item):
        """Retire un élément de la liste et affiche une notification."""
        if item in self:
            super().remove(item)
            print(f"Retiré {item} de la liste.")
        else:
            print(f"{item} n'est pas dans la liste.")

    def pop(self, index=-1):
        """Retire et renvoie un élément de la liste et affiche une notification."""
        if self:
            item = super().pop(index)
            print(f"Retiré {item} de la liste.")
            return item
        else:
            print("La liste est vide.")
            raise IndexError("pop from empty list")


# Test de la classe VerboseList
if __name__ == "__main__":
    vl = VerboseList()

    # Test de append
    vl.append(5)
    vl.append("hello")

    # Test de extend
    vl.extend([1, 2, 3])

    # Test de remove
    vl.remove(5)
    vl.remove(10)  # Tente de retirer un élément qui n'existe pas

    # Test de pop
    vl.pop()
    vl.pop(0)

    # Affichage de la liste finale
    print("Liste finale:", vl)
