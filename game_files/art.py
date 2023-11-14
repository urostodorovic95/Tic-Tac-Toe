import copy
from .board_engine import board

guide = """
######################
How to specify fields:   
   0    1    2              
0: ⃞ | ⃞ | ⃞           
   -----------
1: ⃞ | ⃞ | ⃞
   -----------
2: ⃞ | ⃞ | ⃞
   -----------
Specify ROW first, then COLUMN.
#######################
"""

def print_board():
    """Loops through the numerical board and "pretty prints" the board for user."""
    board_copy = copy.deepcopy(board)
    for index_board, row in enumerate(board):
        for index_row, element in enumerate(row):
            if element == 0:
                board_copy[index_board][index_row] = "⃞"
            elif element == 1:
                board_copy[index_board][index_row] = "❌"
            else:
                board_copy[index_board][index_row] = "⭕"

    for row in board_copy:
        print(" | ".join(row))
        print("------------")

