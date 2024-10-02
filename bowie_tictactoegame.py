import random

#initialisation of identifiers
board = [['-' , '-' , '-'],
         ['-' , '-' , '-'],
         ['-' , '-' , '-']]
game_counter = 0
game_run= True

#a function to print important information, description and instructions of the Tic-Tac-Toe game
def instructions():
    print('''
A Computer Versus Human Tic-Tac-Toe Computer Game designed by Bowie Chew.

Rules of the Tic Tac Toe Game:
-The first player to get 3 of the same symbols in a row (up, down, across or diagonally) is the winner.
-There are two symbols, being X and O in a Tic-Tac-Toe game.
-Based on the rules of the Tic-Tac-Toe game, X gets to move first, followed by O.
-The program will ask for the preferred symbol being X or O.
-If human player selects X, the human player will be prompted to move first.
-If human player selects O, the computer player will be prompted to move first.

Here are the instructions to play:
-The Tic-Tac-Toe game is played on a grid that contains 3 rows and 3 columns.
-For the player to move their symbol, the program will ask for a [row number] and a [column number].
-Spaces that are occupied cannot be selected and the program will ask for another input.

-An example of each space's input is shown below:

-[ROW, COLUMN]

-   C       C       C
    O       O       O
    L       L       L
    U       U       U
    M       M       M
    N       N       N
 
    1       2       3
    ↓       ↓       ↓

 +------+-------+-------+
  [1,1] | [1,2] | [1,3]    ← R O W 1
 +------+-------+-------+
  [2,1] | [2,2] | [2,3]    ← R O W 2
 +------+-------+-------+
  [3,1] | [3,2] | [3,3]    ← R O W 3
 +------+-------+-------+
''')
    #to allow players to read each and every instructions prior to starting the game
    input('Press any key to continue...')

#a function to prompt user for preferred symbol and inisialise   
def player_selection():
    inp = str(input('\nWhat is your preferred symbol? (X/O): '))
    
    #an if statement to allow user to choose their preferred symbol
    #or else return to function and repeat player_selection function if conditions of either X or O is not met
    if inp.upper() == 'X':
       human = 'X'
       computer = 'O'
       current_player = human
       return human, computer, current_player
    elif inp.upper() == 'O':
        human = 'O'
        computer = 'X'
        current_player = computer
        return human, computer, current_player
    else:
        print('Invalid input')
        return player_selection()
    
#a function to print board of 3 rows and 3 columns using the for loop function    
def print_board (board):
    for x in range (3):
        print('\n+---+---+---+')
        print('|',end = '')
        for y in range (3):
            print('', board[x][y], end = ' |')
    print('\n+---+---+---+')

#a function to prompt user to input row number and column number and update the board with the chosen symbol if conditions are met.
def human_input(board, symbol):
    print("\nIt's your turn.")
    row = int(input('Enter the row number: '))
    col = int(input('Enter the column number: '))

    #an if statement to check if row number and column number is within the range of board (1-3)
    #or else return to human_input function if conditions of either X or O is not met 
    if (row >=1 and row <=3) and (col >=1 and col <=3):

        #a nested if statement to check if space of inputted row and column is occupied and  replace empty space with symbol
        #or else return to human_input function if conditions of either X or O is not met 
        if board[row-1][col-1] == '-':
            board[row-1][col-1] = symbol
            return row, col

        else:
            print('\nOops that position is occupied, please try again.')
            print_board(board)
            return human_input(board, symbol)

    else:
        print('\nThe value is out of range, Please input 1-3 for row number and column number respectively.')
        print_board(board)
        return human_input(board, symbol)

#a function to switch current_player from human to computer and vice versa for each round 
def switch_player ():
    #global is used to update current_player as initialised by player_selection
    global current_player

    if current_player == human:
        current_player = computer

    elif current_player == computer:
        current_player = human

#a function to loop for a random row and column number until if statement is able to return row and column
def computer_input (board, symbol):

    while current_player == symbol:
        row = random.randint (1,3)
        col = random.randint (1,3)

        #an if statement to check if random row and column number is occupied
        if board[row-1][col-1] == '-':
            print("\nIt's the computer's turn.")
            print('The computer is thinking....')
            board[row-1][col-1] = symbol
            return row, col

#a function to check for win
def check_win(board):
    outcome = []

    #appending the 3 rows of symbols as string into outcome
    for x in range(3):
        outcome.append(board[x][0] + board[x][1] + board[x][2])

    #appending the 3 columns of symbols as string into outcome
    for x in range(3):
        outcome.append(board[0][x] + board[1][x] + board[2][x])

    #appending the 2 diagonals of symbols as string into outcome
    outcome.append(board[0][0] + board[1][1] + board[2][2])
    outcome.append(board[0][2] + board[1][1] + board[2][0])

    #an if statement to check if 3 consecutive symbols of string in the list is the same,
    #print win/lose message and return true for that function according to chosen symbol.
    if 'XXX' in outcome:

        if human == 'X':
            print('\nCongratulations, you won the game with symbol X!')
            return True

        elif computer == 'X':
            print('\nSorry, you lost the game with symbol O!')
            return True

    elif 'OOO' in outcome:

        if human == 'O':
            print('\nCongratulations, you won the game with symbol O!')
            return True

        elif computer == 'O':
            print('\nSorry, you lost the game with symbol X!')
            return True

#a function to append text into file named game_log.txt with information such as Move Count, Computer(C)/Human(H), Row, Column, Piece (X/O)
def move_log (move_counter, player_type, symbol, row, col):
    with open('logfile_ 21056445.txt', 'a') as move_log:
        move_log.write('\n' + str(move_counter) + ', ' + player_type + ', ' + str(row) + ', ' + str(col) + ', ' + symbol + '.')
        
#a function to start the game using if statement to see if human or computer is the current player to start with it.
def start ():
    move_counter=0
    #If current_player is human, while loop will start with human_input, followed by check_win, switch_player, computer_input and print_board
    if current_player == human:
        print_board(board)
        #while game_run = True and break when check_win function is returned true
        #or else print tie message if move_counter reaches 9 and no one wins. 
        while game_run:
            row, col = human_input(board, human)
            move_counter+=1
            move_log (move_counter, 'H', human, row, col)
            print_board(board)

            if check_win(board) == True:
                with open('logfile_ 21056445.txt', 'a') as game_log:
                    game_log.write('\nThe winner is ' + human + '!\n')
                break
            
            elif move_counter == 9:
                print ('\nIts a tie!')
                with open('logfile_ 21056445.txt', 'a') as game_log:
                    game_log.write('\nIts a tie.\n')
                break

            switch_player()
            row, col = computer_input(board, computer)
            move_counter+=1
            move_log (move_counter, 'C', computer, row, col)
            print_board(board)

            if check_win(board) == True:
                with open('logfile_ 21056445.txt', 'a') as game_log:
                    game_log.write('\nThe winner is ' + computer + '!\n')
                break

            switch_player()

    #else if current_player is computer, while loop will start with computer_input, followed by check_win, switch_player, human_input and print_board
    elif current_player == computer:
        #while game_run = True and break when check_win function is returned true
        #or else print tie message if move_counter reaches 9 and no one wins. 
        while game_run:
            row, col = computer_input(board, computer)
            move_counter+=1
            move_log (move_counter, 'C', computer, row, col)
            print_board(board)

            if check_win(board) == True:
                with open('logfile_ 21056445.txt', 'a') as game_log:
                    game_log.write('\nThe winner is ' + computer + '!\n')
                break

            elif move_counter == 9:
                print ('\nIts a tie')
                with open('logfile_ 21056445.txt', 'a') as game_log:
                    game_log.write('\nIts a tie.\n')
                break

            switch_player()
            row, col = human_input(board, human)
            move_counter+=1
            move_log (move_counter, 'H', human, row, col)
            print_board(board)

            if check_win(board) == True:
                with open('logfile_ 21056445.txt', 'a') as game_log:
                    game_log.write('\nThe winner is ' + human + '!\n')
                break
            
            switch_player()

#Initial calling of functions to run game with instructions
instructions() 
human, computer, current_player = player_selection()
game_counter+=1
with open('logfile_ 21056445.txt', 'w') as game_log:
    game_log.write('Game ' + str(game_counter))
start()


#a function to prompt player whether to play again and return the function as true if yes,
#return the function as false if no and return to function if input is neither Y or N
def restart ():
    inp = input('Do you want to play again? (Y/N): ')
    if inp.upper() == 'Y':
        return True
    elif inp.upper() == 'N':
        print('Thanks for playing!')
        return False
    else:
        print('Invalid input')
        return restart()
    
#while loop to call restart function and if returned true similarly to first calling of function but without instructions
while restart() == True:
    board = [['-' , '-' , '-'],
             ['-' , '-' , '-'],
             ['-' , '-' , '-']]
    human, computer, current_player = player_selection()
    game_counter +=1
    with open('logfile_ 21056445.txt', 'a') as game_log:
            game_log.write('\nGame ' + str(game_counter))
    start()
