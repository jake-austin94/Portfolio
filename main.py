from functions import draw_board, check_turn, check_for_win
import os

positions = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}
game_on = True
complete = False
turn = 0
prev_turn = -1

while game_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(positions)
    if prev_turn == turn:
        print("This is not a valid spot, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press e to quit")
    choice = input()
    if choice == "e":
        game_on = False

    elif str.isdigit(choice) and int(choice) in positions:
        if not positions[int(choice)] in {"X", "O"}:
            turn += 1
            positions[int(choice)] = check_turn(turn)

    if check_for_win(positions):
        game_on, complete = False, True
    if turn > 8:
        game_on = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(positions)

if complete:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("It's a draw.")

print("Thanks for playing!")

