## aoc 2023 - day 3 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *
#  012
#0123456

def check_str(pos,d):
    n='x'
    if pos[0] in INTS and pos[2] in INTS:
        if pos[1] == '.':
            first = int(d[0:3].strip('.'))
            second = int(d[4:].strip('.'))
            print('[!!!]')
            return first+second
        else:
            n=pos
    elif pos[0] in INTS:
        if pos[1]=='.':
            n=d[0:3]
        elif pos[2]=='.':
            n=d[1:4]
        else: 
            n=d[2:5]
    elif pos[1] in INTS:
        if pos[0]=='.'and pos[2]=='.':
            n=pos[1]
        elif pos[0]=='.':
            n=d[3:6]
        elif pos[2]=='.':
            n=d[1:4]
        else:
            print(pos)
            n=pos
    elif pos[2] in INTS:
        if pos[1]=='.':
            n=d[4:]
    else:
        print(pos, d)
        exit(0)
    if n == 'x':
        print(pos,d)
    
    n=int(str(n).strip('.'))
    
    return n
    
def symbol_points(symbols):
    symbol_points = []
    for line in range(len(input)):
        for character in range(len(input[line])):
            if input[line][character] in symbols:
                symbol_points.append([line, character])
    return symbol_points

def udlr(x,y):
    up = input[y-1][x-1:x+2]
    down = input[y+1][x-1:x+2]
    left = input[y][x-1]
    right = input[y][x+1]
    return up, down, left, right

def get_points(up,down,left,right,x,y,points):
    if up!='...': points[0]=(check_str(up,input[y-1][x-3:x+4]))
    if down!='...': points[1]=(check_str(down,input[y+1][x-3:x+4]))
    if left!='.': points[2]=(int(input[y][x-3:x].strip('.')))
    if right!='.': points[3]=(int(input[y][x+1:x+4].strip('.')))
    return points

## part one ##
def part_one():
    symbols = get_symbols(input)
    sps = symbol_points(symbols)
    total=0
    for point in sps:
        y,x = point
        up,down,left,right = udlr(x,y)
        points = get_points(up,down,left,right,x,y,[0,0,0,0])
        total+=sum(points)
    print(total)    
    return

## part two ##
def part_two():
    pointsum = 0
    sps = symbol_points(['*'])
    for point in sps:
        y,x = point
        points=udlr(x,y)
        adjs = [p for p in points if p!='.' and p!='...']
        if len(adjs)==2:
            up, down, left, right = points
            p = get_points(up,down,left,right,x,y,[1,1,1,1])
            pointsum+=(p[0]*p[1]*p[2]*p[3])
    print(pointsum)
    return

test_input = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

input = read_file('input.txt')
#input=test_input
part_one() # 521778 (too low) 528799
part_two() # 80387047 (too low)