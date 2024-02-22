#initializes a dictionarie with the keys 'name', 'age' & 'country' & their respective values.

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
country = str(input("Please enter your country: "))

dictionarie = {"name":name, "age":age, "country": country}
print("Edad:",dictionarie['age'])