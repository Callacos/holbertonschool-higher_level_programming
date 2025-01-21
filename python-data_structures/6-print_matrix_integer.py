#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Args:
        matrix: 2D list of integers (default empty matrix [[]])
    """
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end=" " if i < len(row) - 1 else "")
        print()
