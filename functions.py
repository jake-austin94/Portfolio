def draw_board(position):
    board = (f"|{position[1]}|{position[2]}|{position[3]}|\n"
             f"|{position[4]}|{position[5]}|{position[6]}|\n"
             f"|{position[7]}|{position[8]}|{position[9]}|")
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_for_win(position):
    if (position[1] == position[2] == position[3]) \
            or (position[4] == position[5] == position[6]) \
            or (position[7] == position[8] == position[9]):
        return True
    elif (position[1] == position[4] == position[7]) \
            or (position[2] == position[5] == position[8]) \
            or (position[3] == position[6] == position[9]):
        return True
    elif (position[1] == position[5] == position[9]) \
            or (position[3] == position[5] == position[7]):
        return True
    else:
        return False
