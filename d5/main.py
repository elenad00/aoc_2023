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

def part_one(run_seeds):
    s2s = clean_block(input[1])
    s2f = clean_block(input[2])
    f2w = clean_block(input[3])
    w2l = clean_block(input[4])
    ltt = clean_block(input[5])
    tth = clean_block(input[6])
    htl = clean_block(input[7])

    min = 9999999999999999999
    seed=0
    for seed in run_seeds:
        soil=block(s2s,seed)
        fert=block(s2f,soil)
        wate=block(f2w,fert)
        ligh=block(w2l,wate)
        temp=block(ltt,ligh)
        humi=block(tth,temp)
        loca=block(htl,humi)
        if loca<min:
            min=loca
            seed=seed
    print(min,seed)
    print('---')
    
test_input = read_file('test.txt','\n\n')
input = read_file('input.txt', '\n\n')
#input=test_input
seeds = ((input[0].strip('\n')).split(': '))[1]
seeds = [int(x) for x in seeds.split(' ')]

i=0
total=len(seeds)
while i<total:
    new_seeds = []
    start = seeds[i]
    s_range = seeds[i+1]
    new_seeds=[start+i for i in range(s_range)]
    i+=2
    new_seeds.sort()
    print("finding m loc")
    part_one(new_seeds) # 261,668,924
# part_2 - 350,004,378 too high


'''
seeds: 
 302673608 467797997 
1787644422 208119536 
 143576771  99841043 
4088720102 111819874 
 946418697  13450451 
3459931852 262303791 
2913410855 533641609 
2178733435  26814354 
1058342395 175406592


2041142901 113138307 
'''