# try:
#     print(10 / 0)
# except Exception as e:
#     print(f"An error occurred: {e}")

#
# file = open("example.txt", "r")
# print(file.read())

try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found! check location or file name")
finally:
    if 'file' in locals():
        file.close()
