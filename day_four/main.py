from aoc_utils import *

def get_wins_lines(line):
    winning, card_numbers = line.split(': ')[1].split(' | ')  
    winning = get_list(winning)
    card_numbers = get_list(card_numbers)
    return winning, card_numbers

def get_match_count(winning, card_numbers):
    card_points = 0
    for i in range(len(winning)):
        if winning[i] in card_numbers:
            card_points+=1
    return card_points

def get_list(input_str):
    inp_list = input_str.replace('  ',' ').split(' ')
    if '' in inp_list: inp_list.remove('')
    return inp_list 

def part_one():
    stack_points = 0
    for line in inp_text:
        winning, card_numbers = get_wins_lines(line)
        card_points = get_match_count(winning, card_numbers)
        if card_points!=0:
            card_points=2**(card_points-1)
        stack_points+=(card_points)
        
    print(stack_points) # 25010

def part_two():
    inp_text=test_input
    generated_cards = {}
    card_runs={}
    for i in range(len(inp_text)):
        generated_cards[i]=0
        card_runs[i]=1
    
    for l in range(len(inp_text)):
        winning, card_numbers = get_wins_lines(inp_text[l])
        card_points = get_match_count(winning, card_numbers)
        print(card_points)
        generated_cards[l]=card_points
    
    print('---')
    
    for line in generated_cards:
        s=0
        print(card_runs[line])
        while s<card_runs[line]<6:
            for card in range(line, line+generated_cards[line]):
                card_runs[card]+=1
            s+=1    
    
    #for pile in win_dec: print(pile+1, generated_cards[pile])
      

test_input = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]
inp_text = read_file('input_2.txt')

part_two()

