#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import math as m
# Enter year and day
puzzle = Puzzle(2019, 1)
data = puzzle.input_data
d = data.split('\n')


######################################################################
#   Part 1
######################################################################
def get_fuel_required(data:List) -> int:
    
    total_fuel = 0
    for i in range(len(d)):
        total_fuel += m.trunc(int(d[i]) / 3) - 2
    return total_fuel

puzzle.answer_a = get_fuel_required(d)

######################################################################
#   Part 2
######################################################################
def bla(data:List) -> int:
    y = 0
    for i in range(len(d)):
        x = int(d[i])
        b = m.trunc(x/3)-2
        while b != 0:
            if b < 0:
                b = 0
                break
            y += b
            b = m.trunc(b/3)-2
    return y


# puzzle.answer_b = 
