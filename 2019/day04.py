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
puzzle = Puzzle(2019, 4)
data = puzzle.input_data
d = data.split('-')


######################################################################
#   Part 1
######################################################################
def foo():
    l = list(range(int(d[0]), int(d[1])))
    x = []
    for i in l:
        number = str(i)
        c = Counter(number)
        if int(number[0]) <= int(number[1]) <= int(number[2]) <= int(number[3]) <= int(number[4]) <= int(number[5]):
            if len(c.most_common()) < 6:
                x.append(i)

    return len(x)

# puzzle.answer_a =

######################################################################
#   Part 2
######################################################################

n = ['1','2','3','4','5','6','7','8', '9']
def bar():
    l = list(range(int(d[0]), int(d[1])))
    x = []
    flag = False
    for i in l:
        number = str(i)
        c = Counter(number)
        if int(number[0]) <= int(number[1]) <= int(number[2]) <= int(number[3]) <= int(number[4]) <= int(number[5]):
            mc = c.most_common()
            if len(mc) < 6:
                for j in n:
                    if c[j] == 2:
                        flag = True
                        break
                if flag:
                    x.append(i)
                    flag = False
    return len(x)
               
                        
                        


# puzzle.answer_b = 
