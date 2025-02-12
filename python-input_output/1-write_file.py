#!/usr/bin/python3
def write_file(filename="", text=""):
	"""Écrit une chaîne de caractères dans un fichier texte (UTF8).

	Args:
		filename (str): Le nom du fichier à écrire. Par défaut, une chaîne vide.
		text (str): La chaîne de caractères à écrire dans le fichier. Par défaut, une chaîne vide.

	Comportement:
		Ouvre le fichier en mode écriture avec encodage UTF-8
	"""
	with open(filename, mode='w', encoding='utf-8') as f:
		return f.write(text)