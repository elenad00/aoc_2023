## aoc 2023 - day 11 ##
##     by elena d    ##

## imports
import sys
import os
from math import sqrt
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def get_length(a,b):
    return sqrt(a**2 + b**2)

## part one ##
def part_one():
    galaxy = []
    i = 1
    # add rows
    for line in input:
        galaxy.append(line)
        if line.count('.') == len(line): galaxy.append(''.join(['.' for l in range(len(line))]))
    # add columns
    i = 0
    while i < len(galaxy):
        line = [galaxy[v][i] for v in range(len(galaxy))]
        if '#' not in line:
            for g in range(len(galaxy)):
                galaxy[g] = galaxy[g][0:i]+'.'+galaxy[g][i:]
            i+=1
        i+=1
    # print galaxy
    
    points = []
    for y in range(len(galaxy)):
        for x in range(len(galaxy[0])):
            if galaxy[y][x]=='#': points.append([y,x])    
 
    s = 0
    for i in range(len(points)):
        cy,cx = points[i]
        for y,x in points[i:]:
           a=y-cy
           b=x-cx
           length = abs(a)+abs(b)
           print(length)
           s+=length
        print('---')
    print(s)
    return

## part two ##
def part_two():
    return

test_input = []
input = read_file('test.txt')
part_one()
part_two()