# Author - Biju
# Date - 2021/01/23
# Strategic
"""
board
display board
play game
check win
    check rows
    check columns
    check diagonals
check tie
flip player
"""
# --------Global Variables-------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whose turn is
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tix tac toe


def play_game():

    """Display initial board"""
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "Y":
        print("Hello " + winner + " You Won the match.")
    elif winner == None:
        print("Your match has been Tie.")

# Handle a single turn of an arbitrary player


def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_win()
    check_for_tie()


def check_for_win():
    # set up global variables
    global winner
    """Check rows"""
    row_winner = check_rows()

    """Check column"""
    column_winner = check_columns()

    """Check diagonals"""
    diagonals_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return


def check_rows():
    # set up globals variables
    global game_still_going
    # check if any of the rows all the same value (and is not)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or Y)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set up globals variables
    global game_still_going
    # check if any of the rows all the same value (and is not)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any columns does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or 0)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set up globals variables
    global game_still_going
    # check if any of the rows all the same value (and is not)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    # If any Diagonals does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # Return the winner (X or 0)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    # If the current player was x, then change it to 0
    if current_player == "X":
        current_player = "Y"
    # If the current_player was 0 then change it to x
    elif current_player == "Y":
        current_player = "X"
    return


play_game()
