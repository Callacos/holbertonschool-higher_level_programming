#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
	# Check if the index is valid
	if idx < 0 or idx >= len(my_list):
		return my_list

	# Delete the item at the specified index
	del my_list[idx]

	# Return the modified list
	return my_list
