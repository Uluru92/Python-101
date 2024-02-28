"""
Write a script that takes a sentence from the user and returns:

the number of lower case letters
the number of uppercase letters
the number of punctuations characters
the total number of characters
Use a dictionary to store the count of each of the above.

Note: ignore all spaces.

Example input:

I love to work with dictionaries!
Example output:

Upper case: 1
Lower case: 26
Punctuation: 1
Total chars: 28
"""
import pathlib

sentence = input("Please enter a sentence: ")

upper_counter = 0
lower_counter = 0
puntuation_counter = 0
digit_counter = 0
total_chars_counter = 0

for letter in sentence:
    if letter.isupper():
      upper_counter += 1
    elif letter.islower():
      lower_counter += 1
    elif letter.isdigit():
      digit_counter += 1
    elif letter.isspace():
      continue
    else:
      puntuation_counter += 1

total_chars_counter = upper_counter+lower_counter+digit_counter+puntuation_counter
print(f"Upper case: {upper_counter}\nLower case: {lower_counter}\nPunctuation: {puntuation_counter}\nTotal chars: {total_chars_counter}")

#just to check something!