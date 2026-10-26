import os

os.system("cls")

files = os.listdir()

read = -1

com = ""

running = True

while running == True:
    os.system("cls")
    if read == -1 :  
        for i in range(len(files)) :
            print(str(i)+". "+files[i]+"\n")
    elif read == -2:
        print("You will never know my secrets \n LOSER \n I am better!")
    else:
        print(files[read])
        os.system("start "+files[read])
    com = input("").lower()
    if com.isdigit() == True:
        read = int(com)
    else:
        if com == "back" :
            read = -1
        elif com == "quit" or com == "stop" or com == "close":
            running = False
            os.system("cls")
        elif com == "secret" :
            read = -2
        else:
            for i in range(len(files)) :
                if com == files[i]:
                    read = i
