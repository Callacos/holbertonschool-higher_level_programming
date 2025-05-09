#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (UTF8) """
    with open(filename, "a", encoding="utf-8") as f:
        write = f.write(text)
        return len(text)
