# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib
import shutil

new = pathlib.Path.cwd().joinpath("python-101-main","13_modules-and-automation")
old = pathlib.Path.cwd().joinpath("13_modules-and-automation_copy")

for f in old.iterdir():
    if f.suffix == ".py":
        print(f.suffix)
        shutil.move(f, old.joinpath(new))

print("done with the files summon names")



