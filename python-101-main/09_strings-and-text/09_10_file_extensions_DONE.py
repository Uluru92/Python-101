# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

# use negative range [-4:]

file_1_ext = file_1[-4:]
file_2_ext = file_2[-4:]
file_3_ext = file_3[-4:]
file_4_ext = file_4[-4:]

if file_1_ext != ".pdf":
    print("the file 1 is not a pdf document")
if file_2_ext != ".pdf":
    print("the file 2 is not a pdf document")
if file_3_ext != ".pdf":
    print("the file 3 is not a pdf document")
if file_4_ext != ".pdf":
    print("the file 4 is not a pdf document")