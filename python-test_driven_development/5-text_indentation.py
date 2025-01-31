#!/usr/bin/python3
"""
This module contains a function that indents text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue
        
        if char == '\n':
            result += char
            skip_space = True
        else:
            skip_space = False
            result += char
            
        if char in punctuation:
            result += "\n\n"
            skip_space = True

    lines = result.split('\n')
    for i, line in enumerate(lines):
        print(line.strip(), end="")
        if i < len(lines) - 1:
            print()

