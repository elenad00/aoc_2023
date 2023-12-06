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
    s2s = clean_block(input[1])
    s2f = clean_block(input[2])
    f2w = clean_block(input[3])
    w2l = clean_block(input[4])
    ltt = clean_block(input[5])
    tth = clean_block(input[6])
    htl = clean_block(input[7])

    seed_loc = {}

    for seed in seeds:
        soil=block(s2s,seed)
        fert=block(s2f,soil)
        wate=block(f2w,fert)
        ligh=block(w2l,wate)
        temp=block(ltt,ligh)
        humi=block(tth,temp)
        loca=block(htl,humi)
        # print('se so fe wa li te hu lo')
        # print('-----------------------')
        # print(seed,soil,fert,wate,ligh,temp,humi,loca)
        # print('-----------------------\n')
        seed_loc[loca]=seed

    print(min(seed_loc.items()))
    
test_input = read_file('test.txt','\n\n')
input = read_file('input.txt', '\n\n')

#input=test_input
seeds = ((input[0].strip('\n')).split(': '))[1]
seeds = [int(x) for x in seeds.split(' ')]

i=0
while i<len(seeds):
    new_seeds = []
    start = seeds[i]
    s_range = seeds[i+1]
    for v in range(s_range):
        new_seeds.append(start+v)
    i+=2
    new_seeds.sort()
    seeds=new_seeds
    print("finding m loc")
    part_one() # 261668924
