print ("Challenge #2: Number Guessing Game!!!!")
#Generate a random number between 1 and 20
import random
number = random.randint(1, 20)
number = int(number)
contador = int (0)
guess = int(27)
#Ask the user to guess the number
while number != guess:
#provide feedback to the user if their guess is too high, too low, or correct.
    guess = input("Guess a number between 1 and 20: ")
    guess = int(guess)
    contador += 1
    if guess > number:
        print("Wrong! Too high!!")
    elif guess < number:
        print("Wrong! Too low!!")
    elif guess == number:
        print("Number of attempts:")
        print(contador)
        break
#Allow the user to keep guessing until they correctly guess the number.
#Display the number of attempts it took to guess correctly.