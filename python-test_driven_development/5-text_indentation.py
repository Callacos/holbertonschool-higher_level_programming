#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints a text with 2 new lines after ".?:" characters.
    
    Args:
        text (str): The input text to process.
        
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Parcourir chaque caractère de la chaîne
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Nettoyer les espaces au début et à la fin des lignes
    lines = result.splitlines()
    cleaned_lines = [line.strip() for line in lines]
    cleaned_text = "\n".join(cleaned_lines)

    print(cleaned_text, end="")
