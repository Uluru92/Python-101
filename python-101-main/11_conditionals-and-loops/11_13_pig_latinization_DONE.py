# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.

# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.

text = "You would never guess"

new_text = ""
new_word = ""
word = ""
for i in text:
    if i != " ":
        word += i
    new_word += word
    word = ""
    if i == " ":
        new_text += new_word[1:] + new_word[0]+"AY "
        new_word =""
print(new_text)
    
    
