#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 3)

data = puzzle.input_data.split()

######################################################################
#   Part 1
######################################################################
def calc_tree_count(right_direction, down_direction):
    tree_count = 0
    right = 0

    i = 0
    while i < len(data):
        j = right
        row = data[i]*len(data)
        if i != 0 and j < len(row):
            if row[j] == '#':
                tree_count += 1
        right += right_direction
        i += down_direction

    return tree_count


#puzzle.answer_a = tree_count


######################################################################
#   Part 2
######################################################################
def multiply_different_results():
    result = calc_tree_count(1, 1)*calc_tree_count(3, 1)*calc_tree_count(5, 1)*calc_tree_count(7, 1)*calc_tree_count(1,2)
    return result

res = multiply_different_results()

#puzzle.answer_b = res