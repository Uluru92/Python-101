#Create a program that does the following:
#Initializes two sets with some common elemments.
#Prints the union of the two sets.

import random

num_1 = random.randint(1,2)
num_2 = random.randint(2,4)
num_3 = random.randint(1,2)
num_4 = random.randint(2,4)

set_1 = {num_1,num_2}
set_2 = {num_3,num_4}
set_union = set_1 | set_2


print("set 1:",set_1,"\nset 2:",set_2)
print("The union of the two sets:",set_union)
