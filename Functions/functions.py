# #basic function
# def greet():
#     print("this is a greet function. Helloo")
#
# greet()


# #function with parameters
# def add(a, b):
#     return a + b
#
# result = add(7, 3)
# print(result)

# #default arguments
# def greet(name="User"):
#     print(f"Hello, {name}!")
#
# greet()
# greet("Ram")


##
# def describe_person(name, age):
#     print(f"{name} is {age} years old.")
#
# describe_person(age=26, name="ram")

# # Named arguments or artibary arguments when we dont know how many to pass
# def sum_numbers(*args):
#     return sum(args)
#
# print(sum_numbers(1, 2, 3, 2,1))

#keyword arguments
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="ram", age=26, role="qa",job="none")

