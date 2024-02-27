# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import pathlib

#Create lists: main folder / sub folder 1 / sub folder 2
list_main = []
list_subfolder_1 = []
list_subfolder_2 = []

# Set up the folder we where we want to do the searching 
main_path = str(input("Please enter the folder path where you want to search: "))
main_path = pathlib.Path(main_path)

print("My actual path is:",main_path)

for file in main_path.iterdir():

    if file.suffix == ".jpg":
        list_main.extend([file])

    if file.is_dir():
        subfolder_1_path = pathlib.Path(file)

        for file_sub1 in subfolder_1_path.iterdir():

            if file_sub1.suffix == ".jpg":
                list_subfolder_1.extend([file_sub1])

            if file_sub1.is_dir():
                subfolder_2_path = pathlib.Path(file_sub1)

                for file_sub2 in subfolder_2_path.iterdir():

                    if file_sub2.suffix == ".jpg":
                        list_subfolder_2.extend([file_sub2])

print("List of images en main folder: ")
for png_file in list_main:
    print(list_main)

print("List of images in subfolder 1: ")
for png_file in list_subfolder_1:
    print(list_subfolder_1)

print("List of images in subfolder 2: ")
for png_file in list_subfolder_2:
    print(list_subfolder_2)