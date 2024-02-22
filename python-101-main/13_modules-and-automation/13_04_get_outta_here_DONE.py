# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import sys

counter = 0
word_user = 0

while counter < 1:
    word_user = str(input("enter a text:"))
    if word_user == "quit":
        print("System quitting....")
        sys.exit()