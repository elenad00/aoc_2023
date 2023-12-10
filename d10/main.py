## aoc 2023 - day 10 ##
##     by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    visited = [start]
    x,y=start
    nesw = [pipe_grid[y-1][x],pipe_grid[y][x+1],pipe_grid[y+1][x],pipe_grid[y][x-1]]
    print(nesw)       
    for key in next_pipe:
        c = 0
        for i in range(4):
            if nesw[i] in next_pipe[key][i]: c+=1
        if c==2:break
    type=c
    print(type, key)
    current=start
    coords=[0,0]
    while coords!=start:
        
    next = 
    
    
    return

## part two ##
def part_two():
    return

input = read_file('test.txt')
pipes = {'|':1,'-':2,'L':3,'J':4,'7':5,'F':6,'.':0,'S':9}
c = [[],[1,5,6],[1,3,4],[2,4,5], [2,3,6]]
next_pipe = {
    1:[c[1],c[0],c[2],c[0]],
    2:[c[0],c[3],c[0],c[4]],
    3:[c[1],c[3],c[0],c[0]],
    4:[c[1],c[0],c[0],c[4]],
    5:[c[0],c[0],c[2],c[4]],
    6:[c[0],c[3],c[2],c[0]],
}
pipes = {
    1:{[0,1],[0,-1]},
    2:{[1,0],[-1,0]},
    3:{[0,1],[1,0]},
    4:{[0,1],[-1,0]},
    5:{[-1,0],[0,-1]},
    6:{[0,-1],[1,0]}
}

start = []
pipe_grid = []
for line in input: print(list(line))
for line in input:
    line = [pipes[x] for x in line]
    pipe_grid.append(line)
    if 9 in line:
        start=[pipe_grid.index(line), line.index(9)]
    print(line)

part_one()
part_two()