# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

"""
# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there
"""

import pathlib
import shutil

work_space = pathlib.Path.cwd()
work_space_module1 = pathlib.Path.cwd().joinpath("python-101-main","13_modules-and-automation")
work_space.joinpath("13_modules-and-automation_copy1").mkdir(exist_ok=True)

for f in work_space_module1.iterdir():
    if f.suffix == ".py":
        print(f.name) #returns the path name
        print(f.stem) #returns the path without the extension
        #shutil.move(f, work_space.joinpath("13_modules-and-automation_copy"))
        
print("done with the files summon names")



