#!/usr/bin/env python2.7
#Guessing game. Program that simulates the guessing of a number between 1 and 50. This is one of the assignments from Notebook3 in Bui's Elements of Computing I class

import random

print "Program that simulates a guessing game between 1 and 50"

number = random.randint(1, 50)
guesses = 0

while guesses < 5:
    guess = int(raw_input("Enter an integer from 1 to 50: "))
    guesses +=1
    print "This is your %d guess" %guesses
    if guess < number:
        print "Guess is too low. Try again."
    elif guess > number:
        print "Guess is too high. Tru again."
    elif guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print "You guess it in : ", guesses + " guesses"

if guess != number:
    number = str(number)
    print "The secret number was",  number
