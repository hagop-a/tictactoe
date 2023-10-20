import tkinter as tk
from tkinter import messagebox

# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

gameStillGoing = True
winner = None
currentPlayer = "X"

# Create a window for Tic Tac Toe
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the board
buttons = [tk.Button(root, text="-", font='Arial 20', width=5, height=2, command=lambda i=i: handleTurn(currentPlayer, i))
           for i in range(9)]

# Display buttons in a grid
for i, button in enumerate(buttons):
    row = i // 3
    col = i % 3
    button.grid(row=row, column=col)

def handleTurn(player, position):
    global currentPlayer
    print(currentPlayer + "'s turn.")

    if board[position] == "-" and gameStillGoing:
        board[position] = player
        buttons[position].config(text=player)
        checkIfGameOver()
        flipPlayer()
    elif not gameStillGoing:
        messagebox.showinfo("Game Over", "Game is already over!")
    else:
        messagebox.showinfo("Invalid Move", "This position is already taken!")

def checkIfGameOver():
    global gameStillGoing
    if checkForWin() != None:
        gameStillGoing = False
        messagebox.showinfo("Game Over", winner + " Wins!")
    elif checkIfTie():
        gameStillGoing = False
        messagebox.showinfo("Game Over", "It's a Tie!")


def checkForWin():
    global winner
    for i in range(3):
        numRow = i * 3
        numColumn = i
        if board[numRow] == board[numRow + 1] == board[numRow + 2] != "-":
            winner = board[numRow]
            return winner
        elif board[numColumn] == board[numColumn + 3] == board[numColumn + 6] != "-":
            winner = board[numColumn]
            return winner
        elif i == 0 and board[0] == board[4] == board[8] != "-":
            winner = board[0]
            return winner
        elif i == 2 and board[2] == board[4] == board[6] != "-":
            winner = board[2]
            return winner
    return None


def checkIfTie():
    return "-" not in board


def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Start the GUI event loop
root.mainloop()
