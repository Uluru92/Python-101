# Move and rename all .png files on your Desktop
# Identify all screenshots on your Desktop

import pathlib

# Find the path to my Desktop
desktop_path = pathlib.Path('C:/Users/User/Desktop')
print("My actual path is:",desktop_path)

# Create a new directory
screenshots_path = pathlib.Path("C:/Users/User/Desktop/screenshots") # create the path objetc
screenshots_path.mkdir(exist_ok=True) # create the object folder y si ya existe evitar el error con exist_ok
counter = 1

# Move and rename all screenshots
for file in desktop_path.iterdir():
    if file.suffix == ".jpg": #This way we filter the jpg files
        print(file.name)

        new_file_name = f"renamed_file_{counter}{file.suffix}" #assigns the new file name to a variable
        print("new file name: "+new_file_name)
        
        new_file_path = desktop_path / new_file_name #create the new path for the new file
        file.rename(new_file_path)
        counter += 1

        new_moved_file_path = screenshots_path.joinpath(new_file_path.name) # creates a new path for each file
        
        new_file_path.replace(new_moved_file_path) # Move the screenshot there oldpath.replace(newpath)

#TO IMPROVE: IF ALREADY DONE, WE DONT WANT TO REPLACE THE NEXT SCREENSHOTS FILES TO MOVE AND REPLACE THE ONES ALREADY THERE!....