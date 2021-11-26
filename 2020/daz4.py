#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import re

# Enter year and day
puzzle = Puzzle(2020, 4)

pre_data = puzzle.input_data

data = puzzle.input_data.split('\n\n')

#print(data)
######################################################################
#   Part 1
######################################################################
def create_passport_object(passport):
    pp = {}
    for p in passport:
        pp[p.split(':')[0]] = p.split(':')[1]
    return pp

temp1 = []
passport_list = []
for d in data:
    temp1.append(d.replace('\n', ' ')) # Replace \n with space so that you can really distinguish between passports. 
    # Really Dumb mistake on your part.

for t in temp1:
    passport_list.append(t.split())

print(passport_list)


temp3 = []
for x in passport_list:
    passport_object = create_passport_object(x)
    temp3.append(passport_object)

valid = 0
for p in temp3:
    keys = list(p.keys())
    condition_length_years = len(p["byr"]) == 4 and len(p["iyr"]) == 4 and len(p["eyr"]) == 4
    condition_range_years = 1920 <= int(p["byr"]) <= 2002 and \
        2010 <= int(p["iyr"]) <= 2020 and \
        2020 <= int(p["eyr"]) <= 2030
    condition_hgt_cm = "cm" in p["hgt"] and \
        150 <= int(re.match(r"\d+gm", p["hgt"])) <= 193 
    condition_hgt_in = "in" in p["hgt"] and \
        59 <= int(re.match(r"\d+gm", p["hgt"])) <= 76
    condition_hcl = len(p["hcl"]) == 7 and '#' in p["hcl"]
    # TODO: Finish condition of haircolor with regexp
    # print (keys)
    if len(keys) == 8:
        valid += 1
        #print(p)
    elif len(keys) == 7 and not "cid" in keys:
        valid += 1
        #print("Misses cid ", p)
    


puzzle.answer_a = valid


######################################################################
#   Part 2
######################################################################


# puzzle.answer_b = 