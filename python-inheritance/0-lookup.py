#!/usr/bin/python3
def lookup(obj):
    """Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet à inspecter

    Returns:
        Liste des attributs et méthodes de l'objet
    """
    return dir(obj)
