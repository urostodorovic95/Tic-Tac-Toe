from .board_engine import board

def check_consecutive(lst: list) -> int:
    """Return a number if a list contains only that number;
    Return False otherwise"""
    if len(set(lst)) == 1:
        return lst[0]
    return False


def map_board_diagonally() -> list:
    """Map the array diagonally."""
    diagonals = []
    temp_1 = []
    temp_2 = []
    for n in range(3):
        temp_1.append(board[n][n])
        temp_2.append(board[n][2-n])
    diagonals.append(temp_1)
    diagonals.append(temp_2)
    return diagonals


def map_board_vertically() -> list:
    """Map the array vertically (both directions)"""
    verticals = []
    for num in range(3):
        temp_lst = [row[num] for row in board]
        verticals.append(temp_lst)
    return verticals


def is_board_populated():
    if any(0 in sublist for sublist in board):
        return False
    return True


def check_winner():
    mapped = board + map_board_vertically() + map_board_diagonally()
    for lst in mapped:
        if check_consecutive(lst):
            return check_consecutive(lst)
        
