#!/usr/bin/env python3

import random as rand

def newNumber():
    newNumber.x = rand.randint(1,5)
def newGuess():
    newGuess.guess = int(input("Guess a number!"))
# code to test newNumber()
# newNumber()
# print(newNumber.x)
win = 0

def startGame():
    # newNumber()
    if newNumber.x == newGuess.guess:
        print("You guessed right! New game!")
        global win
        win += 1
        print("Total wins:" + str(win))
        newNumber()
        newGuess()
        startGame()
    elif newNumber.x > newGuess.guess:
        print("You guessed too low!")
        newGuess()
        startGame()
    elif newNumber.x < newGuess.guess:
        print("You guessed too high")
        newGuess()
        startGame()
newNumber()
newGuess()
startGame()
