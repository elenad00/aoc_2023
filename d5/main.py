## aoc 2023 - day 5 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def clean_block(block):
    return (block.replace(':','').replace('\n', ',')).split(',')[1:]

def block(block,var):
    new=var
    for line in block:
        dest, source, length = [int(x) for x in line.split(' ')]
        difference = dest-source
        if source<=var<=source+length:
            new=var+difference
            return new
    return new

def part_one():
    blocks = []
    for i in range(1,8):
        blocks.append(clean_block(input[i]))
    min = seeds[0]
    for seed in seeds:
        prev = seed
        for b in blocks:
            new = block(b,prev)
            prev=new
        if prev<min: min=prev
    print(min)
    
def part_two():
    return

test_input = read_file('test.txt','\n\n')
input = read_file('input.txt', '\n\n')
seeds = [int(x) for x in (input[0].split(': ')[1].split(' '))]

part_one() # 261668924