# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = input("Write some text: ")
letter = str(input("pick 1 letter from the text your text: "))
result = ""

print("String input: ", string)
print("Letter input: ", letter)


counter_i = 0

for i in string:
    if i == letter:
        result += str(counter_i)+" "
        counter_i = int(counter_i)
    counter_i += 1
print("Result: ", result)