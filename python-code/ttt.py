import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
board = [0] *9

playing = True

turn = 1

def show(array):
    txt = []
    num = 1

    for i in array:
        if i == 0:
            txt.append(num)
        elif i == 1:
            txt.append("X")
        elif i == 2:
            txt.append("O")
        num += 1

    print("Player ", turn, " turn")
    print(txt[0]," ",txt[1]," ",txt[2])
    print(txt[3]," ",txt[4]," ",txt[5])
    print(txt[6]," ",txt[7]," ",txt[8])

def win():

    for i in [0,3,6]:
         if board[i] != 0 and board[i] == board[i+1] and board[i] == board[i+2]:
             return board[i]
         
    for i in [0,1,2]:
         if board[i] != 0 and board[i] == board[i+3] and board[i] == board[i+6]:
             return board[i]
         
    if board[0] != 0 and board[0] == board[4] and board[0] == board[8]:
             return board[0]
    
    if board[6] != 0 and board[6] == board[4] and board[6] == board[2]:
             return board[6]

    c = 0
    for i in range(len(board)):
        if board[i] == 0:
            c += 1

    if c == 0:
        return("tie")

    return("no")
                
show(board)

while playing == True:
    clear_console()

    show(board)
    inp = int(input("choose a num 1-9: "))

    if inp <= 9 and inp >=1:
        if board[inp-1] == 0:
            board[inp-1] = turn
            if turn == 1:
                turn = 2
            else :
                turn = 1
        else:
            print("already taken")
    else:
        playing = False
    
    if win() != "no":
        clear_console()

        show(board)

        if win() == "tie":
            print("its a tie")
        else:
            print("player ", win(), " wins")

        playing = False
