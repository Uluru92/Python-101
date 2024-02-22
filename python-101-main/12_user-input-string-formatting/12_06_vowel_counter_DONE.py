# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

string = str(input("Please enter a text: "))

for i in string:
    if i in "aeiou":
        print("the vowel:", i, "appeared", string.count(i),"times")
    elif i == " ":
        print("the space:", i, "appeared", string.count(i),"times")
