#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2016, 1)

# north is y axis +
# east is x axis +
# south is y axis -
# west is x axis -

north = 0
east = 1
south = 2
west = 3

data = puzzle.input_data.replace(' ','').split(',')

######################################################################
#   Part 1
######################################################################

# calculate distance from origin to building
def calculate_distance_to_building(data) -> int:
    player_pos = [0,0] #coordination that we'll use
    state = north

    for i in range(len(data)):
        pos = data[i]
        val = int(pos[1:])
        # nach R oder L
        if state == north:
            # nach osten oder westen
            if pos[0] == 'R':
                player_pos[0] += val
                state = east
            else:
                player_pos[0] -= val
                state = west

        elif state == east:
            # nach süden oder norden
            if pos[0] == 'R':
                player_pos[1] -= val
                state = south
            else:
                player_pos[1] += val
                state = north

        elif state == south:
            # nach westen oder osten
            if pos[0] == 'R':
                player_pos[0] -= val
                state = west
            else:
                player_pos[0] += val
                state = east
        elif state == west: 
            # nach norden oder süden
            if pos[0] == 'R':
                player_pos[1] += val
                state = north
            else:
                player_pos[1] -= val
                state = south
    

    return abs(player_pos[0]) + abs(player_pos[1])


# puzzle.answer_a = 


######################################################################
#   Part 2
######################################################################


# puzzle.answer_b = 