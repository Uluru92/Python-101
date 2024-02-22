# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.
# or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = " Solution is: "
solution2 =" Solution2 is: "
number = "0123456789"

#solution 1
for char in secret:
    if char != "0" and char != "1"and char != "2"and char != "3"and char != "4"and char != "9"and char != "8"and char != "7":
        solution += str(char)
print(solution)

#solution 2
for char in secret:
    if char not in number:
        solution2 += str(char)
print(solution2)
       