"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    # Initilize dictionary
    moves = {}
    for move in range(1, MAX_REMOVE+1):
        moves[move] = 0
        for test_try in range(TRIALS):
            current_items = num_items
            current_items -= move
            while True:
                opp_move = random.randint(1, MAX_REMOVE)
                current_items -= opp_move
                if current_items <= 0:
                    break
                my_move = random.randint(1, MAX_REMOVE)
                current_items -= my_move
                if current_items <= 0:
                    moves[move] += 1
                    break
    v=list(moves.values())
    k=list(moves.keys())
    max_wins = k[v.index(max(v))]
    return max_wins


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(21)