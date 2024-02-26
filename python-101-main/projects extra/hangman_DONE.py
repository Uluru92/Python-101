# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script: mirror
# Print an explanation to the user.
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello".
# Ask for user input.

hang_word = "_ _ _ _ _ _"

print("- + - + - Hang Game - + - + -\nYou have 10 attempsts to guess the pre-defined word.\nYou can only enter 1 letter at a time.\nLets starts!\n"+hang_word)

hide_word = "letras"



number_list = ["0","1","2","3","4","5","6","7","8","9"]
guess = None
counter_fails = 0
used_words = []

while guess == None:

    guess = (input("Guess a letter: "))

    if type(guess) == str:

        if guess in number_list:
            print("Remenber: You cannot enter numbers or simbols.")
                        
        if len(guess) > 1:
            print("Remember, you can only digit 1 letter at a time!")

        if len(guess) == 1:
                        
            if guess in used_words:
                print(f"You already tried the letter {guess}...try again! ")
            
            elif guess in hide_word:
                old_space = hide_word.find(guess)*2         
                new_hang_word = hang_word[:old_space]  + guess + hang_word[old_space+1:]
                print(new_hang_word)

                hang_word = new_hang_word

                if "_" not in hang_word:
                    print("You won!")
                    exit(0)  # Successful exit


            elif guess not in hide_word:
                print(f"The letter {guess} is NOT part of the hidden word...")
                counter_fails += 1
                print(f"You missed {counter_fails} times...")

                if counter_fails == 5:
                    print(f"You lost!")
                    exit(0)  # Successful exit
    
    else: 
        print("Remenber: You cannot enter numbers or simbols.")
    
    used_words.append(guess)
    guess = None

  

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word

# filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it