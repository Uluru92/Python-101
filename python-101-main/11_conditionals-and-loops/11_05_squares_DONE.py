# Write a script that prints out all the squares of numbers from 1 to 50.
# Use a `for` loop that demonstrates the use of the `range()` function.




square_numbers = "the squares of numbers from 1 to 50: \n"
counter_number = 0

for number in range(51):
     square_numbers += "Number: "+str(counter_number)+ "     |    Square: "+str(number*number)+ " \n"
     counter_number += 1

print (square_numbers)