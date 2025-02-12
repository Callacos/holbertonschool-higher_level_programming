#!/usr/bin/python3
"""Module pour lire un fichier texte (UTF8) et afficher son contenu sur stdout."""


def read_file(filename=""):
    """Lit un fichier texte (UTF8) et affiche son contenu sur stdout """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
