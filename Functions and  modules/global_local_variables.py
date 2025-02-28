#
# def func():
#     x = 10  # Local variable
#     print(x)
#
# func()


# x = 5  # Global variable
#
# def func():
#     print(x)
#
# func()


x = 5
# Global variable
print(x)
def modify():
    global x
    x = 10
    print(x)

modify()
print(x)
