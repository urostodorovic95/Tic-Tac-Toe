board = \
 [[0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]]


def update_board(new_value):
    """Updates the numerical board with a 1 for X and 2 for O;
    Updated field is chosen by user."""
    indices = [int(num) for num in input('Choose a field: ').strip().replace(" ", "")]
    try:
        update_field = board[indices[0]][indices[-1]]
        if update_field == 0 and update_field != new_value:
            board[indices[0]][indices[-1]] = new_value
        else:
            print("Field is Occupied! Try again!")
            update_board(new_value)
    except IndexError:
        print("That's an invalid index! Remember: row=0:2, column=0:2")
        update_board(new_value)

