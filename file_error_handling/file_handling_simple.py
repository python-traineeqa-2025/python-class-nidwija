# file = open("example.txt", "r")
# content = file.read()
# file.close()  # Must manually close the file


with open("example.txt", "w") as x:
    x.write()  # File closes automatically
'''
r- reads from file
w - write mode 
a - append mode
x - exclusive creation mode
'''