# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

word_e = s[2]
word_g = s[5]
word_s = s[31]
word_f = s[-9]
word_i = s[73]
word_t = s[16]
word_u = s[58]
word_r = s[6]
word_b = s[33]
word_a = s[7]
word_d = s[12]
"""
Recipe: Golden Scrambled Eggs with Fig Toasts and butter
eggs + figgs + butter + Bread
"""

print("Recipe Golden Scrambled Eggs with Fig Toasts and butter:\n"+word_e+word_g+word_g+word_s, "+", word_f+word_i+word_g+word_g+word_s, "+",word_b+word_u+word_t+word_t+word_e+word_r, "+",word_b+word_r+word_e+word_a+word_d)