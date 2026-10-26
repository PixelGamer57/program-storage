import color as c
import os

play = True

turn = 1

cols = [1,2,5]
board = []

for i in range(6*7):
    board.append(0)

def show(inp):
    os.system("cls")
    t = ""
    for i in range(len(board)):
        t = t + c.color(cols[board[i]])
        if (i+1)%6 == 0:
            t = t + "\n"
    print(t)

def detectWin():
    win = 0
    for i in range(0,36):
        if board[i] == board[i+1]:
            win = board[i]

    if win != 0:
        play == False
        print("Player " + str(win) + " won!")
    return

while play == True:
    show(board)
    p = min(6,int(input("Player : " +str(turn)+ " input 1-6 : \n"))-1)
    board[p] = turn
    while p < 36 and board[p+6] == 0 :
        board[p] = 0
        board[p+6] = turn
        p += 6
        show(board)
    detectWin()
    if turn == 1 :
        turn = 2
    else:
        turn = 1
