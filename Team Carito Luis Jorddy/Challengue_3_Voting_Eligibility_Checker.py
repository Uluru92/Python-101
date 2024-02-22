Age = int(input("Please enter your Age: "))
citizen = int(input("Are you a citizen?\nYes: Type 0\nNo: Type 1\nAnswer: "))

if Age < 18 or citizen == 1:
    print("You are not elegible to vote!")
else:
    print("You are elegible to vote!")