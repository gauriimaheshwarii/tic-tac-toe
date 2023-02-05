game_status = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
cell_remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def choose_sign():
    global player1_sign
    global player2_sign
    is_correct = False

    while (not is_correct):
        player1_sign = input(f"{player1}, please choose your sign (X or O): ")
        if (player1_sign != 'X' and player1_sign != 'O'):
            print("Uh Oh! Please enter a correct character! \n")
        else:
            is_correct = True

    if (player1_sign == 'X'):
        player2_sign = 'O'
    else:
        player_2_sign = 'X'

    print(f"{player1}'s Sign: {player1_sign}")
    print(f"{player2}'s Sign: {player2_sign} \n")

def print_turn():
    print(f"{turn}'s turn!")

def print_game():
    print("   |   |   ")
    print(f" {game_status[0]} | {game_status[1]} | {game_status[2]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {game_status[3]} | {game_status[4]} | {game_status[5]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {game_status[6]} | {game_status[7]} | {game_status[8]} ")
    print("   |   |   ")
    print(" ")

def position_choice():
    choice = 'wrong'

    while (choice not in cell_remaining):
        choice = input("Please enter the position you want to play your mark in (1 - 9): ")
        print(" ")

        if (not choice.isdigit()):
            print("Err! Are you sure that's a correct position? \n")
            continue
        else:
            choice = int(choice) - 1
            
        if (choice not in cell_remaining):
            print("Err! Are you sure that's a correct position? \n")

    return choice

def change_status(position):
    global turn
    if (turn == player1):
        game_status[position] = player1_sign
        turn = player2
    else:
        game_status[position] = player2_sign
        turn = player1
    index = cell_remaining.index(position)
    cell_remaining.pop(index)

def check_tie():
    flag = True
    global is_game_over
    for cell in game_status:
        if (cell == ' '):
            flag = False
    if flag:
        is_game_over = True
        display_tie()

def display_tie():
    print("The game has been tied! Thanks for playing!")
    print_game()
    
def check_win():
    global is_game_over
    if (game_status[0] == game_status[3] == game_status[6] != ' ' or game_status[1] == game_status[4] == game_status[7] != ' ' or \
        game_status[2] == game_status[5] == game_status[8] != ' ' or game_status[0] == game_status[1] == game_status[2] != ' ' or \
        game_status[3] == game_status[4] == game_status[5] != ' ' or game_status[6] == game_status[7] == game_status[8] != ' ' or \
        game_status[0] == game_status[4] == game_status[8] != ' ' or game_status[2] == game_status[4] == game_status[6] != ' '):
        is_game_over = True
        display_win()

def display_win():
    print("CONGRATULATIONS!!")
    print(f"{turn} won the game🎉 \n")
    print_game()

def play_game():
    choose_sign()

    while (not is_game_over):
        print_turn()
        print_game()
        position = position_choice()
        change_status(position)
        check_win()
        check_tie()

print("\n Welcome to Tic-Tac-Toe! ")
print("\t\t -by Gauri Maheshwari \n")  
player1 = input("Player 1, please enter your name: ")
print(" ")
player2 = input("Player 2, please enter your name: ")
print(" ")

player1_sign = None
player2_sign = None
is_game_over = False
turn = player1

play_game()
