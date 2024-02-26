import pathlib

# Find the path to my Desktop
desktop_path = pathlib.Path('C:/Users/User/Desktop')
print("My actual path is:",desktop_path)

# Create a new folder
screenshots_path = pathlib.Path("C:/Users/User/Desktop/screenshots") # create the path objetc
screenshots_path.mkdir(exist_ok=True) # create the object folder y si ya existe evitar el error con exist_ok


# List all the files on there
for file_path in desktop_path.iterdir():
    if file_path.suffix == ".png": #This way we filter the png files
        print(file_path.name)
        new_file_path = screenshots_path.joinpath(file_path.name) # creates a new path for each file
        file_path.replace(new_file_path) # Move the screenshot there oldpath.replace(newpath)