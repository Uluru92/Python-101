# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = str(input("Please enter your honest opinion: "))

opinion_sarcastic = ""
counter = 2

for i in opinion:
    if counter%2 == 0:
        opinion_sarcastic += i.upper()
    elif counter%2 != 0:
        opinion_sarcastic += i.lower()        
    counter += 1

#    if opinion[i]%2 != 0:
#        opinion_sarcastic += i.upper()

print(opinion_sarcastic)