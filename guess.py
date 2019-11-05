#!/usr/bin/env python3

import random as rand


x = rand.randint(1,5)
guess = int(input("Guess a number!"))

def check(x, guess):
    if x == guess:
        print("You guessed right!")
        win=0
        win += 1
        print("Total wins:" + str(win))
    elif x > guess:
        print("You guessed too low!")
        guess = int(input("Guess a number!"))
        check(x, guess)
    elif x < guess:
        print("You guessed too high")
        guess = int(input("Guess a number!"))
        check(x, guess)

check(x, guess)
