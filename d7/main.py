## aoc 2023 - day 7 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    hand_weight = {}
    hands = input.keys()
    for hand in hands:
        full_hand = hand
        hand = set(list(hand))
        amms = [full_hand.count(x) for x in hand]
        if len(hand) == 5:
            weight = 0
        elif len(hand) == 1:
            weight = 5
        elif len(hand) == 2:
            weight = 4
        elif len(hand) == 3:
            if 3 in amms:
                weight = 3
            if amms.count(2) == 2:
                weight = 2
        elif len(hand) == 4:
            weight = 1
        hand_weight[full_hand] = weight
    print(hand_weight)
    return

## part two ##
def part_two():
    return

card_vals = {
    'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, 
    '9':8, '8':7, '7':5, '6':5, '5':4, 
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
    input[hand]=score

input = test_input
part_one()
part_two()