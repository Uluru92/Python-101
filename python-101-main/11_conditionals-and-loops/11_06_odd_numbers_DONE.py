# Using a `for` loop, print out all odd numbers from 1 to 100.


odd_numbers = str()

for number in range(101):
    if number%2 != 0:
        odd_numbers += str(number)+" "
print("the odd_numbers are: "+odd_numbers)