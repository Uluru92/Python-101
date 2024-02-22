# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string_text = str(input("Please write a text: "))
letter_to_replace = string_text[0]
symbol = str(input("Please enter a symbol: "))
Result = "Result:"

new_string_text = string_text.replace(letter_to_replace, symbol)

print(Result,new_string_text)
