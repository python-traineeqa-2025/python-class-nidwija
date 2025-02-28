try:
    with open("newfile.txt", "x") as file:
        file.write("This file is created using 'x' mode.")
    print("File created successfully!")
except FileExistsError:
    print("File already exists!")
