# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

number = int(input("Please enter a number between 1 and 1000000000: "))


if number%3 == 0: 
    print("The number is divisible by 3, the result is: ", number/3)
else:
    print("The number is not divisible by 3. Bye!")