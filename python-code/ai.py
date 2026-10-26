import random
import os

letters = list("abcdefghijklmnopqrstuvwxyz")

word = ""

lists = open("ai_save.txt").read().splitlines()

words = lists[0].split(",")

notWords = lists[2].split(",")

exit = False

def newWord(length: int):
    thisword = []
    while len(thisword) < length:
        thisword.append(letters[random.randrange(0,len(letters))])


    word = "".join(thisword)
    if words.__contains__(word) or notWords.__contains__(word):
        word = newWord(length)
    
    return word

while not exit:
    os.system("cls")
    word = newWord(random.randint(3,7))
    answer = input(f"Is '{word}' a real word? \n").lower()

    if answer == "y" or answer == "yes":
        words.append(word)
    elif answer == "stop":
        print(" ".join(words))
        exit = True
    elif answer == "sort":
        words.sort()
        notWords.sort()
        open("ai_save.txt", "w").write(",".join(words) + "\n" + "\n" + ",".join(notWords))
        print(" ".join(words))
        exit = True
    else:
        notWords.append(word)
    
    open("ai_save.txt", "w").write(",".join(words) + "\n" + "\n" + ",".join(notWords))
