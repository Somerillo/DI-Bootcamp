print("Welcome to tic tac toe (R)")

# define blank board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# define winner combinations
win_combination = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

def print_board(board_temp):
    """
    It prints on screen the board`s state
    """
    print("\n")
    # print(board[0][0], " | ", board[0][1], " | ", board[0][2])
    print("   1   2   3")
    print("1 ", " | ".join(col for col in board_temp[0])) # prints first row
    print("  -----------")
    print("2 ", " | ".join(col for col in board_temp[1])) # prints 2nd row
    print("  -----------")
    print("3 ", " | ".join(col for col in board_temp[2])) # prints 3rd row
    print("\n")

def player_input(board_temp, player):
    """
    It writes on the board cells
    """
    while True:
        print(f"Player {player}`s turn")
        col = input("Input column number (1 to 3):")
        row = input("Input row number (1 to 3):")

        if not col.isdigit() or not row.isdigit():
            print("Only digits, try again")
            continue # return to the bucle`s sart point

        col = int(col) - 1
        row = int(row) - 1

        if not (0 <= row <= 2) or not (0 <= col <= 2):
            print("Cell out of range, try again")
            continue # return to the bucle`s sart point

        elif board_temp[row][col] != " ":
            print("Cell already used, try again")
            continue # return to the bucle`s sart point
            
        else:
            board_temp[row][col] = player
            break

    return board_temp

def check_board(board_temp):
    """
    It checks the board visual interface and returns two lists for X`s and O`s positions
    """
    list_X = []
    list_O = []
    
    for row in range(3):
        for col in range(3):
            if board_temp[row][col] == "X":
                list_X.append((row, col))
            elif board_temp[row][col] == "O":
                list_O.append((row, col))
    return list_X, list_O

def game_on(board_temp):
    """
    It runs the whole game
    """
    turn = 0
    
    while True:

        # print board actual state
        print_board(board_temp)

        # check every cell if we have a tie
        if all(" " not in row for row in board_temp):
            print("Match tied, get a life")
            break

        # check for a winner
        positions_X, positions_O = check_board(board_temp)
        if positions_X in win_combination:
            print("Player `X` is the winner, now get a life")
            break
        if positions_O in win_combination:
            print("Player `O` is the winner, now get a life")
            break

        # sets which player`s turn is
        if turn % 2 == 0:
            player = "X"
        else:
            player = "O"

        # input player`s cell of choice
        board_temp = player_input(board_temp, player)
        
        # update counter
        turn += 1

game_on(board)