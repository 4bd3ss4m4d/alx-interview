#!/usr/bin/python3

'''
This module contains the function canUnlockAll(boxes) that determines
if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    This function determines if all the boxes can be opened.

    Args:
        boxes: a list of lists of integers.

    Returns:
        True if all the boxes can be opened, False otherwise.
    '''

    boxes_length = len(boxes)
    keys_set = [0]
    cntr = 0
    i = 0

    while i < len(keys_set):
        set_k = keys_set[i]
        for k in boxes[set_k]:
            if 0 < k < boxes_length and k not in keys_set:
                keys_set.append(k)
                cntr += 1
        i += 1
    return cntr == boxes_length - 1
