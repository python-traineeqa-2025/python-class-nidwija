def greet():
    print("this is a greet function. Helloo")

greet()


def add(a, b):
    return a + b

result = add(5, 3)
print(result)


def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Ram")


def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(age=26, name="ram")

# Named arguments
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 2))


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="ram", age=26, role="qa")

