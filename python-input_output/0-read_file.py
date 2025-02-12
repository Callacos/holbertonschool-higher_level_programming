#!/usr/bin/python3
def read_file(filename=""):
    """Lit un fichier texte (UTF8) et affiche son contenu sur stdout.

    Args:
        filename (str): Le nom du fichier à lire. Par défaut, une chaîne vide.

    Comportement:
        Ouvre le fichier en mode lecture avec encodage UTF-8
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
