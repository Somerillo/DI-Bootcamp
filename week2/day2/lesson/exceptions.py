# print('hello world'))

# my_num = int(input('Gimme a number')) # if a enter a letter i get ValueError

#Try and Except to handle 

#Example about tic tac tow

board = ['-','-','-',
         '-','-','-',
         '-','-','-',]

game_goes_on = True
winner = None

def display_board():
    print("***********")
    for i in range(0,9, 3):
        print('*  ' + board[i] + '|' + board[i+1] + '|' + board[i+2] + '  *')
    print("***********")

def player_input(current_player):
    valid = False
    while not valid:
        position = input(f'{current_player} choose a position from 1 to 9:') 
        try:
            position = int(position)-1      
            if 0 <= position < 9 and board[position] == '-':
                board[position] = current_player
                valid = True
            else:
                print('Invalid position. Choose a number between 1 and 9.')
        except:
            continue


def check_winner():
    global winner
    global game_goes_on    

    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for coord in win_coord:
        if board[coord[0]] == board[coord[1]] == board[coord[2]] != "-":
            winner = board[coord[0]]
            game_goes_on = False
            return winner

    # check tie
    if '-' not in board and winner == None:
        winner = 'Tie'
        game_goes_on = False
        return winner
    
def play_game():
    while game_goes_on:
        display_board()
        players = ['X','O']
        for current_player in players:
            player_input(current_player)
            display_board()
            winner = check_winner()
            if winner == 'Tie':
                return print('Tie')
            elif winner != None:
                return print(f'{winner} won the game')
            
play_game()

#