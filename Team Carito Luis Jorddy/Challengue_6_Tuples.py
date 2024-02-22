#initializes the tuple with 'apple' 'banana' 'orange' 'banana' 'apple'
#counts the occurreccenses of each element and prints a dictionary with the elements as the key
#and its count as the value

#solution
tuple = ['apple', "banana", "orange","banana",'apple']
print("Input: ", tuple)
dictionary = {}
for i in tuple:
        dictionary.update({i:tuple.count(i)})
print("Dictionary:",dictionary)



