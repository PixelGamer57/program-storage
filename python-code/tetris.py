import os 
import time
import color as c
from inputimeout import inputimeout, TimeoutOccurred

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

playing = True

board = [[1]*10 for _ in range(16) ]

i = 1

board[0][0] = 2

move = 0

while playing == True:
    clear()
    for col in range(len(board)):
        cl = []
        for row in range(len(board[col])):
            cl.append(c.color(board[col][row]))
        print("".join(cl))
    
    try:
        m = inputimeout(prompt="", timeout=0.5)
        if m.lower()[0] == "d":
            move = 1
        elif m.lower()[0] == "a":
            move = 2
        
    except TimeoutOccurred:
        move = 0

    if move == 0:
        if i < len(board):
            if board[i] == [1]*10:
                board[i] = board[i-1]
                board[i-1] = [1]*10
            i = i + 1
        else:
            board[0][0] = 2
            i = 1
    elif move == 1:
        for lol in range(1,len(board)):
            board[i][lol] = board[i][lol-1]
        board[i][0] = 1