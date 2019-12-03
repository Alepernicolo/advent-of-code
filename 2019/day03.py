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
puzzle = Puzzle(2019, 3)
data = puzzle.input_data
x = data.split('\n')
wire1 = x[0].split(',')
wire2 = x[1].split(',')



######################################################################
#   Part 1
######################################################################
def count_player_pos(d:List):
    playerpos = list((0, 0))
    l = []
    for i in range(len(d)):
        num = int(d[i][1:])

        if d[i][0] == 'U':
        # positive y
            for j in range(num):
                playerpos[1] += 1
                curr = playerpos[:]
                l.append(tuple(curr))
        elif d[i][0] == 'R':
            # positive x
            for j in range(num):
                playerpos[0] += 1
                curr = playerpos[:]
                l.append(tuple(curr))
        
        elif d[i][0] == 'L':
            # negative x
            for j in range(num):
                playerpos[0] -= 1
                curr = playerpos[:]
                l.append(tuple(curr))
        
        elif d[i][0] == 'D': 
            # negative y
            for j in range(num):
                playerpos[1] -= 1
                curr = playerpos[:]
                l.append(tuple(curr)) 

    return l

l1 = count_player_pos(wire1)
l2 = count_player_pos(wire2)

test = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
t = test.split('\n')
tt1 = t[0].split(',')
tt2 = t[1].split(',')

t1 = count_player_pos(tt1)
t2 = count_player_pos(tt2)

def calc_manhattan_distance(list1:List, list2:List):
    s = set(l1) & set(l2) # to get intersections 
    l = list(s)
    dis = []
    d = 0
    for e in l:
        d = abs(int(e[0])) + abs(int(e[1]))
        dis.append(d)  
    dis.sort()  
    return dis[0]

######################################################################
#   Part 2
######################################################################
# gets points as list and interesection point as tuple
def count_steps_to_intersection(points:List, intersec:tuple):
    seq = []
    if intersec in points:
        counter = 0
        for p in points:
            counter += 1

            #seq.append(p)
            if p == intersec:
                return counter


def find_fewest_to_intersection(list1:List, list2:List):
    s = set(list1) & set(list2)
    l = list(s)
    sums = []
    for i in l:
        c1 = count_steps_to_intersection(list1, i)
        c2 = count_steps_to_intersection(list2, i)
        c3 = c1 + c2
        sums.append(c3)
    sums.sort()
    return sums[0]


# puzzle.answer_b = 
