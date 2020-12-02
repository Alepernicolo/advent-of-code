#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 2)

data = puzzle.input_data.split("\n")
#print(data)
######################################################################
#   Part 1
######################################################################
def parse_password_policy_to_quartuple(data):
    password_plus_policy_list = []
    minimum = 0
    maximum = 0
    letter = ''
    password = ''

    for d in data:
        password_plus_policy = d.split(": ")
        password = password_plus_policy[1]
        for e in range(0,len(password_plus_policy)):
            # Refers to policy
            if e % 2 == 0:
                policy = password_plus_policy[e].split()
                for n in range(0,len(policy)):
                    if n % 2 == 0:
                        minimum_maximum = policy[n].split("-")
                        minimum = int(minimum_maximum[0])
                        maximum = int(minimum_maximum[1])
                    else:
                        letter = policy[n]
        password_plus_policy_list.append((minimum, maximum, letter, password))    
    return password_plus_policy_list           

tuple_list = parse_password_policy_to_quartuple(data)
"""mini = 0
maxi = 0
letter = ''
password = ''
valid = 0
invalid = 0
for t in tuple_list:
    mini = t[0]
    maxi = t[1]
    letter = t[2]
    password = t[3]
    if password.count(letter) >= mini and password.count(letter) <= maxi:
        print("Password: {}, Letter: {}, Min: {}, Max: {}, Count: {}".format(password, letter, mini, maxi, password.count(letter)))
        valid += 1
    else:
        invalid += 1
print("Valid passwords: {}".format(valid))
print("Invalid passwords: {}".format(invalid))"""

#puzzle.answer_a = valid


######################################################################
#   Part 2
######################################################################
first_pos = 0
second_pos = 0
letter = ''
password = ''
valid = 0
invalid = 0
for t in tuple_list:
    first_pos = t[0]
    second_pos = t[1]
    letter = t[2]
    password = t[3]
    if (password[first_pos-1] == letter) ^ (password[second_pos-1] == letter):
        print("Password: {}, Letter: {}, first_pos: {}, second_pos: {}, Count: {}".format(password, letter, first_pos, second_pos, password.count(letter)))
        valid += 1
    else:
        invalid += 1
print("Valid passwords: {}".format(valid))
print("Invalid passwords: {}".format(invalid))


puzzle.answer_b = valid