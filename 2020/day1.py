#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 1)

data = puzzle.input_data.split()
numbers = [int(x) for x in data]
######################################################################
#   Part 1
######################################################################

"""
difference = list(map(lambda x: 2020 - x, numbers))
sum_tuple = ()
product = 0

for d in difference:
    if d in numbers:
        sum_tuple = (numbers[numbers.index(d)], numbers[difference.index(d)])

print(sum_tuple)
product = sum_tuple[0] * sum_tuple[1]
print(product)
puzzle.answer_a = product"""


######################################################################
#   Part 2
######################################################################

# x+y+z aus der numbers liste sollen 2020 summiert ergeben

sum_triple = 0
prod_triple = 0
for x in numbers:
    for y in numbers:
        for z in numbers:
            if x != y and x != z and y != z:
                sum_triple = x + y + z
                if sum_triple == 2020:
                    prod_triple = x * y * z
                    break

         

puzzle.answer_b = prod_triple