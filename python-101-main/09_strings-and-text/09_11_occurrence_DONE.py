# Find the index of the first occurrence of the letter `n` in the string.

composer = "Ludvig van Beethoven"
x = 0

for letter in composer:
    if letter != "n":
        x += 1
    else:
        print("The first ocurrence of the letter 'n':", x)
        break
