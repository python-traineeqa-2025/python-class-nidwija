# Open file in write mode

# with open("example.txt", "w") as file:
#     # file.write("Hello, this is a test file.\n")
#     # file.write("This is the second line.")
#     file.write('overwriting the file')

# #
# with open("example.txt", "a") as file:
#     # file.write("Hello, this is a test file.\n")
#     # file.write("This is the second line.")
#     file.write('overwriting the file')
#
with open("example.txt", "x") as file:
    # file.write("Hello, this is a test file.\n")
    # file.write("This is the second line.")
    file.write('overwriting the file')

#
# lines = ["writing lines\n", "this is the second line writing through a list\n"]
#
# with open("example.txt", "w") as file:
#     file.writelines(lines)  # Writes a list of strings

# with open("example.txt", "r") as file:
#     x = file.read()
#     print(x)

# with open("example.txt", "r") as file:
#     for i in file:
#         print(i)
#
# with open("example.txt", "r") as file:
#     first_line = file.readline()
#     print(first_line)

#
# with open("example.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
