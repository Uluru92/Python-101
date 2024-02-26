"""
Population Growth Calculator
Write the necessary code to display the total population count for the next 3 years (without a leap year).

Here are the specifications:

In the country we want to investigate:

The current population is 380,123,456
One person is born every 6 seconds
One person dies every 12 seconds
One person immigrates every 40 seconds
"""

current_population = 380123456
born_period = 1/6 #person/seconds
death_period = 1/12 #person/seconds
imigrate_period = 1/40 #person/seconds
grow_rate = born_period-death_period+imigrate_period

growth_period = 3 #tiempo de analisis
print(f"Growth Period:{growth_period} years")

growth_period = 3*365.25*24*60*60 #seconds
print(f"Growth Period:{growth_period} seconds")

growth_population = growth_period*grow_rate
three_years_population = current_population + growth_population
print("Current population:",current_population)
print("Total growth population",growth_population)
print("Population counter for the next 3 years:",three_years_population)
