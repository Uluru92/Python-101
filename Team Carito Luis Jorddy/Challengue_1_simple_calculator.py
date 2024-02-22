print ("Challenge #1: Simple Calculator")
number1 = int(input("Enter the first number:"))
number1 = int(number1)      
number2 = input("Enter the second number:")
number2 = int(number2)
operation = input("Choose operation: 1. Addition 2.Subtraction 3. Multiplication 4. Division    Enter the number operation:")
operation = int(operation)
if operation == 1:
    print("Result:")
    print(number1 + number2)
elif operation == 2:
    print("Result:")
    print(number1 - number2)
elif operation == 3:
    print("Result::")
    print(number1 * number2)
elif operation == 4:
    print("Result:")
    print(number1 / number2)