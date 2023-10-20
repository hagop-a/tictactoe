import sys

#Global Variables:

# board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

gameStillGoing = True #start game

winner = None #no team won yet

currentPlayer = "X" #initially, it's X's turn



# display board
def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])



def playGame():
    
    #Display initial Board
    displayBoard()
    
    while gameStillGoing:
        
        #handle a single turn of an arbitrary plater
        handleTurn(currentPlayer)
        
        # check fi the game has ended
        checkIfGameOver()
        
        #flip to the other player
        flipPlayer()
    
        #the game has ended
        if winner == "X" or winner == "O":
            print("the winner is " + winner)
            return  
    print("Tie.")

# Handle a single turn of an arbitrary player

def handleTurn(player):
    print(player + "'s turn.")
    print("Choose position from 1-9: ")
    position = sys.stdin.readline().strip()  # Read input directly from stdin
    
    availablePos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while position not in availablePos or board[int(position) - 1] != "-":
        print("Invalid input. Choose position from 1-9: ")
        position = sys.stdin.readline().strip()  # Read input directly from stdin

    position = int(position) - 1
        
    board[position] = player
    displayBoard()

def checkIfGameOver():
    checkForWin()
    checkIfTie()
    
def checkForWin():
    
    # Set up global variable
    global winner
    global gameStillGoing
    
    for i in range(3):
        numRow = (i)*3
        numColumn = i
        
        #check row of index i
        if board[numRow] == board[numRow + 1] == board[numRow + 2] != "-":
            winner = board[numRow] # confirm winner
            gameStillGoing = False #found winner so game is over
            return winner # return winner "x" or "o"
            
        #check column of index i
        elif board[numColumn] == board[numColumn + 3] == board[numColumn + 6] != "-":
            winner = board[numColumn]
            gameStillGoing = False
            return winner
        
        # check diagonal 1
        elif i == 0 and board[0] == board[4] == board[8] != "-":
            winner = board[numColumn]
            gameStillGoing = False
            return winner
        
        #check diagonal 2
        elif i == 2 and board[2] == board[4] == board[6] != "-":
            winner = board[numColumn]
            gameStillGoing = False
            return winner
    winner = None
    return winner

def checkIfTie():
    global gameStillGoing
    
    #check if 
    if "-" not in board:
        gameStillGoing = False
    else: gameStillGoing = True
    return

def flipPlayer():
    global currentPlayer
    if currentPlayer == "X": currentPlayer = "O"
    else: currentPlayer = "X"
    return

playGame()



# board
# display board
# play game
# handle turns
# check win
    # check rows
    # check columns
    # check diagonlas    
# check tie
# flip player

# ROCK PAPER SCISSORS
# have the words on screen
# someway to select rock paper or scissors
# have computer randomly generate RPS
# someway to compare them and decide who wins



    # 012, 345, 678
    # 036, 147, 258
    # 048, 246

## if i == 1, then (1-1)*3 + 1 
# if i == 2, then (2-1)*3 + 1
##
##