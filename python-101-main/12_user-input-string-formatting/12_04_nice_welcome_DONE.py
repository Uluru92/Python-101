# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

user = str(input("Please, enter your name: "))
name = ""

for i in user:
    if i != " ":
        name += i

print("Thank you for participating in my show", name+". \nWelcome!!!") 