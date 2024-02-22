# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number_user = int(input("Please enter a number between 0 and 1000000000: "))

for i in range(1000000001):
    if i == number_user:
        print("The number is", i)
        break