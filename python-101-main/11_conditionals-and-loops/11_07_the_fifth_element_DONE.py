# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

fifth_elements = str()

for number in range(1001):
    if number%5 == 0:
        fifth_elements += str(number)+" "
        
print("Here is every fifth number counting from 1 to 1000: "+ fifth_elements)