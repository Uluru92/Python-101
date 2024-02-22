# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

#SOLUCION1
print("Solución 1:\n",*[i for i in range(10)],"\n",*[i for i in range(10,20)],"\n",*[i for i in range(20,30)],"\n",*[i for i in range(30,40)],"\n",*[i for i in range(40,50)],"\n")

#SOLUCION2
list = " "
for i in range(50):
    if i <50 and i != 10 and i != 20 and i != 30 and i != 40:
        list += str(i)+" "
    elif i == 10:
        list += "\n "+ str(i)+" "
    elif i == 20:
        list += "\n "+ str(i)+" "
    elif i == 30:
        list += "\n "+ str(i)+" "
    elif i == 40:
        list += "\n "+ str(i)+" "
print("Solución 2\n"+list+"\n")

#SOLUCION3

line_1 =  "0  1  2  3  4  5  6  7  8  9 \n"
line_2 =  "10 11 12 13 14 15 16 17 18 19 \n"
line_3 =  "20 21 22 23 24 25 26 27 28 29 \n"
line_4 =  "30 31 32 33 34 35 36 37 38 39 \n"
line_5 =  "40 41 42 43 44 45 46 47 48 49 \n"
print("Solución 3\n"+f"{line_1}{line_2}{line_3}{line_4}{line_5}")
