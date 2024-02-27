"""
Trip Cost Calculator
This is a small project to get yourself warmed up and keep
 training your newly found skills in collecting user input
   and formatting strings.

Create a Python script that asks a user questions in the
 command line. The script should follow the outlined specifications.

Specifications
Receive the following arguments from the user:

Kilometers to drive
Liters-per-kilometer usage of the car
Price per liter of fuel
Calculate the cost of the trip and display it to the
 user in the console. Apply some of the string formatting tricks 
 that you learned about in this course section.
"""

cost_trip = None

km_drive = float(input("Please enter the kilometers to drive(km): ")) #km

liter_per_km = float(input("Please enter thel liters per kilometer usage of the car(l/km): "))  #l/km

price_per_liter = float(input("Please enter the price_per_liter($/l): ")) #$/l

cost_trip = float(km_drive*liter_per_km*price_per_liter)

print(f"The total cost of the trip is: ${cost_trip}")