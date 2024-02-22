# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

number = random.randint(1,10)
first_guess = ""
second_guess = ""
third_guess = ""

print("Welcome to Guess My Number Game!")

first_guess = int(input("Please, enter a number between 1 and 10,\nyou only have 3 opportunities to guess!\nFirst guess: "))

if first_guess != number:
    second_guess = int(input("You missed! Please, try again: "))
    if second_guess != number:
        third_guess = int(input("Last chance! Please, try again: "))
        if third_guess != number:
            print("You lose!:(")
        else:
            print("You won! Cngrtz!!!:)")
    else:
        print("You won! Cngrtz!!!:)")
else:
    print("You won! Cngrtz!!!:)")

