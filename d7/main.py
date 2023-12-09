## aoc 2023 - day 7 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def get_num_hands():
    num_hands = {}
    for hand in input.keys():
        num_hand = [int(card_vals[x]) for x in hand]
        num_hands[''.join([str(v) for v in num_hand])]=hand
    return num_hands

def refine(hands, v):
    nsl = []
    for s in range(1,14):
        new_hand = [h for h in hands if h[v]==s]
        try: new_hand.sort(key=lambda y:y[v+1])
        except: new_hand.sort(key=lambda y:y[v])
        if len(new_hand)==1: 
            nsl+=new_hand
            continue
        elif len(new_hand)==0:
            continue
        elif v<=3:
            nsl+=refine(new_hand, v+1)
            continue
    return nsl

def split_cards():
    lists = [[],[],[],[],[],[],[]]
    hands = input.keys()
    for hand in hands:
        full_hand = hand
        num_hand = [int(card_vals[x]) for x in hand]
        hand = set(list(hand))
        amms = [full_hand.count(x) for x in hand]
        if len(hand) == 5:
            lists[0].append(num_hand)
        elif len(hand) == 4:
            lists[1].append(num_hand)
        elif len(hand) == 1:
            lists[6].append(num_hand)
        elif len(hand) == 2:
            if 4 in amms:
                lists[5].append(num_hand)
            elif 3 in amms:
                lists[4].append(num_hand)
        elif len(hand) == 3:
            if 3 in amms:
                lists[3].append(num_hand)
            elif amms.count(2) == 2:
                lists[2].append(num_hand)
    return lists

# part one
def part_one():
    lists = split_cards()
    new_vals = []
    for hand_group in lists:
        vals=refine(hand_group, 0)
        new_vals+=vals
    num_hands=get_num_hands()
    total = 0
    i = 1
    weights = []
    for val in new_vals:
        print(val)
        val = [str(x) for x in val]   
        val = num_hands[''.join(val)]
        weight = input[val]
        print(val, i, weight)
        cume_weight = i*weight
        weights.append(cume_weight)
        i+=1
    w_sum = sum(weights)
    print(246795406-w_sum)
    return 

## part two ##
def part_two():
    return

card_vals = {
    'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, 
    '9':8, '8':7, '7':6, '6':5, '5':4, 
    '4':3, '3':2, '2':1
}

test_input = {
    '32T3K': 765,
    'T55J5': 684,
    'KK677': 28,
    'KTJJT': 220,
    'QQQJA': 483
}
input = {}
raw_input = read_file('input.txt')
for line in raw_input:
    hand, score = line.split()
    input[hand]=int(score)

#input = test_input
part_one() # 246680660 (too low) 
#            246795406
part_two()