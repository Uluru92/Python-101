# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string_1 = str(input("Give me the 1rst word please: "))
string_2 = str(input("Give me the 2nd word please: "))
string_3 = str(input("Give me the 3rd word please: "))

len_1 = int(len(string_1))
len_2 = int(len(string_2))
len_3 = int(len(string_3))

print("word 1 has:",len_1,"letters")
print("word 2 has:",len_2,"letters")
print("word 3 has:",len_3,"letters")

if len_1 > len_2 and len_1 > len_2:
    print("the longest string is:",string_1,"with",len_1,"letters")
if len_2 > len_1 and len_2 > len_3:
    print("the longest string is:",string_2,"with",len_2,"letters")
if len_3 > len_1 and len_3 > len_2:
    print("the longest string is:",string_3,"with",len_3,"letters")
if len_3 == len_1 and len_3 > len_2:
    print("the longest string are:",string_3, "and", string_1,"with",len_3,"letters")
if len_3 == len_2 and len_3 > len_1:
    print("the longest string are:",string_3,"and", string_2,"with",len_3,"letters")
if len_2 == len_1 and len_2 > len_3:
    print("the longest string are:",string_2,"and",string_1,"with",len_2,"letters")

