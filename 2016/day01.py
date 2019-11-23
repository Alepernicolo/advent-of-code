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

# gets coordinates to building (part 1 relevant)
def get_coordinates_to_building(data) -> List:
    player_pos = [0,0] #coordination that we'll use
    state = north
    positions = []

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
        positions.append(list(player_pos))

    return positions


# puzzle.answer_a = 


######################################################################
#   Part 2
######################################################################
def calculate_abs_twice_visited(data) -> int:
    player_pos = [0,0] #coordination that we'll use
    state = north
    positions = []

    for i in range(len(data)):
        pos = data[i] # entry
        val = int(pos[1:]) # actual number
        
        # nach R oder L
        if state == north:
            x = player_pos[0]
            # nach osten oder westen
            if pos[0] == 'R':
                # this loop adds every coordinate to list from current x to next x + val
                for i in range(x, x + val):
                    player_pos[0]+=1
                    positions.append(list(player_pos))
                state = east
            else:
                for i in range(x, x - val, -1):
                    player_pos[0]-=1
                    positions.append(list(player_pos))
                state = west

        elif state == east:
            y = player_pos[1]
            # nach süden oder norden
            if pos[0] == 'R':
                # this loop adds every coordinate to list from current y to next y - val
                for i in range(y, y - val, -1):
                    player_pos[1]-=1
                    positions.append(list(player_pos))
                state = south
            else:
                for i in range(y, y + val):
                    player_pos[1]+=1
                    positions.append(list(player_pos))
                state = north

        elif state == south:
            x = player_pos[0]
            # nach westen oder osten
            if pos[0] == 'R':
                for i in range(x, x - val, -1):
                    player_pos[0]-=1
                    positions.append(list(player_pos))
                state = west
            else:
                for i in range(x, x + val):
                    player_pos[0]+=1
                    positions.append(list(player_pos))
                state = east
        elif state == west: 
            y = player_pos[1]
            # nach norden oder süden
            if pos[0] == 'R':
                for i in range(y, y + val):
                    player_pos[1]+=1
                    positions.append(list(player_pos))
                state = north
            else:
                for i in range(y, y - val, -1):
                    player_pos[1]-=1
                    positions.append(list(player_pos))
                state = south
    # tuplize inner list pair so that we can count them
    for i in range(len(positions)):
        positions[i] = tuple(positions[i])
    
    # return the manhattan distance of the first entry, cause that is what we're looking for
    res = [k for k, v in Counter(positions).items() if v > 1]
    return abs(res[0][0]) + abs(res[0][1])


# puzzle.answer_b = 