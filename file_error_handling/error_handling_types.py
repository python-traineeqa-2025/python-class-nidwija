# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError as e:
#     print("Error:", e)
#     print("list index is out of range")
#
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print("Error:", e)

'''
stale element exception
no such element found

'''