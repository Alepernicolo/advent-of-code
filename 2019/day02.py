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
puzzle = Puzzle(2019, 2)
data = puzzle.input_data
d = list(map(int, data.split(',')))

######################################################################
#   Part 1
######################################################################
def find_value() -> int:
    d3 = d.copy()
    
    d3[1] = 12
    d3[2] = 2

    opcode = 0
    for i in range(0, len(d3), 4):
        opcode = d3[i]
        if i % 4 == 0:
            if opcode == 1:
                #add
                d3[d3[i + 3]] = d3[d3[i + 1]] + d3[d3[i + 2]]
            elif opcode == 2:
                #multiply
                d3[d3[i + 3]] = d3[d3[i + 1]] * d3[d3[i + 2]]
            elif opcode == 99:
                break
                #halt
    return d3[0]
######################################################################
#   Part 2
######################################################################
def find_val2( d1:int, d2:int) -> int:
    dl = d.copy()
    dl[1] = d1
    dl[2] = d2
    
    # print(d1, d2)

    opcode = 0
    for i in range(0, len(dl), 4):
        opcode = dl[i]
        if i % 4 == 0:
            if opcode == 1:
                #add
                dl[dl[i + 3]] = dl[dl[i + 1]] + dl[dl[i + 2]]
                
            elif opcode == 2:
                #multiply
                dl[dl[i + 3]] = dl[dl[i + 1]] * dl[dl[i + 2]]
                
            elif opcode == 99:
                break
                #halt
    return dl[0]

def find_noun_verb() -> (int, int):
    x = 0
    flag = False
    for noun in range(0, 100):
        for verb in range(0, 100):
            x = find_val2(noun, verb)
            if x == 19690720:
                flag = True
                break
        if flag:
             return (noun, verb)

    


# puzzle.answer_b = 
