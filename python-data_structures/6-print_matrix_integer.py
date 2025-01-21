#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	# Loop through each row in the matrix
	for row in matrix:
		# For each row, print the integers formatted correctly
		for i, num in enumerate(row):
			# Print the number, and add a space if it's not the last in the row
			print("{:d}".format(num), end=" " if i < len(row) - 1 else "")
		# Print a newline after each row
		print()
