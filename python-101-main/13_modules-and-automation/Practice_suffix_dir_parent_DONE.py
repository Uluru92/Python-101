import pathlib

ti_path = pathlib.Path('C:/Users/User/Desktop')

print("My actual path is:",ti_path)

for filepath in ti_path.iterdir():
    if filepath.suffix == ".png": #This way we filter the png files
        print(filepath.name)
        if filepath.is_dir():
            print(f"{filepath} is a directory")
        else:
            print(f"{ti_path} is not a directory")

if ti_path.is_dir():
    print(f"{ti_path}") #this way we confirm is a directory

path_obj = pathlib.Path(ti_path)
print("path_obj:",path_obj)

parent_dir = path_obj.parent
print("path_parent:", parent_dir) #this way we get the Folder where the object Path is, in other words its ''Parent''

