# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

n = int(input("Enter the n value in range(1,n): "))
string = range(n+1)


for i in string:
    if i != 0 and i%3 == 0 and i%5 != 0:
        print("Fizz")
    if i != 0 and i%5 == 0 and i%3 != 0:
        print("Buzz")
    if i != 0 and i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i != 0 and i%3 != 0 and i%5 != 0:
        print(i)
    

    

