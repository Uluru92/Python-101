# Demonstrate how to:
# -------------------
# 1) Convert an int to a float

number_int = 1
print(number_int)

number_float = number_int + 1.2
print(number_float)

# 2) Convert a float to an int

number_float_int = int(number_float)
print(number_float_int)

# 3) Perform division using a float and an int.
print(number_float_int/number_float)

# 4) Use two variables to perform a multiplication.

print(number_float*number_float_int)

# What information is lost during which conversions?
#When transforming a float to an int, it truncates the decimal part
