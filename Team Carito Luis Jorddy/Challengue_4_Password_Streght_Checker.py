Password = input("Please enter a password, it must:\nContain at least 8 characters long\nContain a combination of lowercase and uppercase letters\nContain at least one digit (0-9)\nContain at least one special caracterer (e.g.,@,#,$)\nPassword: ")
Letters = list(Password)
Counter_uppercase = int(0)
Counter_lowercase = int(0)
Counter_numbers = int(0)
Counter_Special_letters = int(0)
Special_letters = {"#", "$", "%", "@"}
Character_long = int(0)
for Letter in Letters:
    if Letter.isupper():
        Counter_uppercase += 1
    elif Letter.islower():
        Counter_lowercase += 1
    elif Letter.isdigit():
        Counter_numbers += 1
    elif any(letter in Special_letters for letter in Password):
        Counter_Special_letters += 1
Character_long = Counter_uppercase + Counter_lowercase + Counter_numbers + Counter_Special_letters
print ("Uppercases: ", Counter_uppercase,"\nLowercases: ", Counter_lowercase,"\nNumbers: ", Counter_numbers,"\nSpecial Digits: ", Counter_Special_letters,"\nCharacter long: ", Character_long)
if Counter_uppercase == 0 or Counter_lowercase == 0 or Counter_numbers == 0 or Counter_Special_letters == 0 or Character_long < 8:
    print("The password is weak, please follow criteria for a strong password")
else:
    print("The password is strong!")