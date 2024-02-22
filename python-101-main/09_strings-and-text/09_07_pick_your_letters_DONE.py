# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

#w=1 e=2 s=7 t=0

word_w = word[1]
word_e = word[2]
word_s = word[7]
word_t = word[0]
word_r = word[6]

print(word_w+word_e,word_s+word_e+word_e,word_t+word_r+word_e+word_e+word_s)
