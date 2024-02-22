# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.


number_user = int(input("Give me a number between 1 and 12 please: "))
if number_user == 1:
    print("the moth number", number_user, "is January")
elif number_user == 2:
    print("the moth number", number_user, "is February")
elif number_user == 3:
    print("the moth number", number_user, "is March")
elif number_user == 4:
    print("the moth number", number_user, "is April")
elif number_user == 5:
    print("the moth number", number_user, "is May")
elif number_user == 6:
    print("the moth number", number_user, "is June")
elif number_user == 7:
    print("the moth number", number_user, "is July")
elif number_user == 8:
    print("the moth number", number_user, "is August")
elif number_user == 9:
    print("the moth number", number_user, "is September")
elif number_user == 10:
    print("the moth number", number_user, "is October")
elif number_user == 11:
    print("the moth number", number_user, "is November")
elif number_user == 12:
    print("the moth number", number_user, "is December")