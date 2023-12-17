## aoc 2023 - day 10 ##
##     by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def get_surround(map, y,x):
    try:
        if y-1>=0: sn = map[y-1][x]
        else: sn = 0
    except: 
        print(y,x)
        exit()
    if x+1<len(pipe_grid): se = map[y][x+1]
    else: se = map[y][x]
    if y+1<len(pipe_grid): ss = map[y+1][x]
    else: ss = map[y][x]
    if x-1>=0: sw = map[y][x-1]
    else: sw = map[y][x]
    return [sn,se,ss,sw]

## part one ##
def part_one():
    visited = [start]
    y,x=start
    pipe_kind = 6#4
    print('---')
    end=0
    while end<(140*140):
        surround = get_surround(pipe_grid,y,x)
        #print(surround)
        moves = pipe_moves[pipe_kind]
        for move in moves:
            my,mx = move
            next_coords = [y+my, x+mx]
            move_index = nesw.index(move)
            next_pipe_v = surround[move_index]
            if next_pipe_v == 9 and len(visited)>8:
                print('ending')
                end = (140*140)+1
            elif next_pipe_v in next_pipe[pipe_kind][move_index]:
                if next_coords not in visited:
                    #print(next_coords)
                    visited.append(next_coords)
                    y, x = next_coords
                    pipe_kind = next_pipe_v
                    break
        end+=1
    steps = (len(visited))/2
    print(steps)
    return visited

## part two ##
def part_two(visited):
    map = [[0]*len(pipe_grid[0]) for i in range(len(pipe_grid))]
    visited.sort()
    for coords in visited:
        y, x = coords
        map[y][x]=1
    
    y = 0
    x = 0
    enclosed = 0
    for row in map:
        for column in row:
            surround = get_surround(map,y,x)
            if surround == [1,1,1,1] and map[y][x]==0:
                enclosed+=1
                try: map[y][x]=1
                except: print(y,x)
            x+=1
        x=0
        y+=1
    print(enclosed)
    return

input = read_file('test.txt')
c = [[],[1,5,6],[1,3,4],[2,4,5],[2,3,6]]
next_pipe = {
    1:[c[1],c[0],c[2],c[0]],
    2:[c[0],c[3],c[0],c[4]],
    3:[c[1],c[3],c[0],c[0]],
    4:[c[1],c[0],c[0],c[4]],
    5:[c[0],c[0],c[2],c[4]],
    6:[c[0],c[3],c[2],c[0]],
}
#             n      e     s     w
n,e,s,w = [[-1,0],[0,1],[1,0],[0,-1]]
nesw = [n,e,s,w]
pipe_moves = {
    1:[n,s],
    2:[e,w],
    3:[n,e],
    4:[n,w],
    5:[s,w],
    6:[s,e],
}
pipe_grid = []
pipes = {'|':1,'-':2,'L':3,'J':4,'7':5,'F':6,'.':0,'S':9}
for line in input:
    line = [pipes[x] for x in line]
    #print(line)
    pipe_grid.append(line)
    if 9 in line:
        start=[pipe_grid.index(line), line.index(9)]
    #print(line)

visited = part_one() # 6842
part_two(visited) #12562 too high
#                  11892 too high
#                    352 too low