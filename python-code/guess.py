import random

number = random.randint(1,100)
guess = ""

isGuessed = False
numberOfGuesses = 0

while isGuessed == False:
    guess = input("Enter your guess: ")
    numberOfGuesses += 1
    if int(guess) > number:
        print("too high")
    elif int(guess) < number:
        print("too low")
    else :
        print("correct")
        print("you took " + str(numberOfGuesses) + " guesses")
        isGuessed = True
