from random import randint

import os
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
#ship_row=[0,0]
#ship_col=[0,0]
#for i in range(2):
#    ship_row[i]=int(input("Enter row:"))
#    ship_col[i]=int(input("Enter col:"))
ship_row = int(input("ENter row"))#random_row(board)
ship_col = int(input("Enter column"))#random_col(board)
#print (ship_row)
#print (ship_col)
os.system('cls')
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print ("Turn",turn+1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
 
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        os.system("pause")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0   or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row-1][guess_col-1] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row-1][guess_col-1] = "X"
    # Print (turn + 1) here!
        print_board(board)
        
        if turn == 3:
            	print ("Game Over")
            	print ("The ship was hidden in:")
            	print ("Row:",ship_row,"Column:",ship_col)
            	board[ship_row-1][ship_col-1]="#"
            	print_board(board)
            	os.system("pause")
