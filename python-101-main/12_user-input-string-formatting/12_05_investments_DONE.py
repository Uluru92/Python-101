# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
#

print("Please enter the following: \n")
invest = int(input("Investment amount ($): "))
interest = int(input("Investment rate (%/year): "))
years = int(input("Number of years to invest:"))
future_value = 0
counter_years = 1

while years >= counter_years:
    future_value += invest*(1+interest/100)
    invest = future_value
    print("The invest at the end of the year", counter_years,"is:", future_value)
    counter_years += 1

print("Future value:",future_value)