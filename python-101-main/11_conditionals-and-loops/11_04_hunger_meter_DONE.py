# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.

hunger = str

while hunger != "big" and hunger != "small":
    hunger = input(str("Declare your hunger leves:\n answer: big / small: "))
    if hunger == "big":
        print("Eat the pizza")
    elif hunger == "small":
        print("Eat the apple")
    elif hunger != str:
        print("remenber your entry must be big/small")
    else:
        print("Don't eat anything")
        