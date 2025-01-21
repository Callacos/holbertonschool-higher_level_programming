#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element at specific position in a copied list.

    Args:
        my_list: The input list
        idx: Position to modify
        element: New element to insert
    Returns:
        New list with modified element, or copy of original if invalid idx
    """
    if my_list is None:
        return None
    
    new_list = my_list.copy()
    
    if idx < 0 or idx >= len(my_list):
        return new_list
        
    new_list[idx] = element
    return new_list
