# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

var_1 = wrong and right
print("variable 1: ", var_1)

var_2 = wrong or right
print("variable 2: ",var_2)

var_3 =  wrong and not right
print("variable 3: ",var_3)

result = var_1 and var_3
print("result variable 1 + variable 2:", result)