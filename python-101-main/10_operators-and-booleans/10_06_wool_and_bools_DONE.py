# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.

sheep_name = input("Give a name to the sheep: ")
wool_state = input("The sheep has wool?\n Answer yes/no: ")
if wool_state == "yes":
    print("the sheep name is",sheep_name,", it has wool")
else:
    print("the sheep name is",sheep_name,", it has not wool")