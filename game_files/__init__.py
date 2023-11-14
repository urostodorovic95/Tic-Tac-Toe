from. art import guide, print_board
from .board_engine import update_board
from .check_winner import *

def alternate_players():
    """Generator function to alternate between X (1) and O (2)"""
    while game:
        yield 1
        yield 2

def game():
    game = True
    player_alternator = alternate_players()

    print(guide)
    while game:
        n = next(player_alternator)
        if n == 1:
            print("❌ plays!")
        else:
            print("⭕ plays!")
        update_board(new_value=n)
        if check_winner():
            if check_winner() == 1:
                print("❌ wins!")
            if check_winner() == 2:
                print("⭕ wins!")
            game = False
        if is_board_populated():
            print("It's a draw.")
            game = False
        print_board()

