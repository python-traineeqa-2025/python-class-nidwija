# Basic String Operations
p = 'car'
r = 'race'

# split/join
b = 'hello my name'
print(b.split(' '))  # Split into a list
o = ['hello', 'hi']
print(','.join(o))  # Join with a separator

print(p.startswith('c'))  # Check if starts with 'c'
print(p.endswith('r'))  # Check if ends with 'r'


print(p.isalpha())  # True (alphabetic)
print(p.isdigit())  # False (numeric)
print("123".isdigit())  # True
print("race123".isalnum())  # True (alphanumeric)

# # String Formatting
# name = "ram"
# age = 26
# print(f"My name is {name} and I am {age} years old.")  # f-string
# print("My name is {} and I am {} years old.".format(name, age))  # .format()
# print("My name is %s and I am %d years old." % (name, age))  # % formatting

# Finding Substrings
print(b.find("name"))  # Index of substring (-1 if not found)
print(b.index("name"))  # Similar to find() but raises an error if not found
print(r.count('r'))  # Count occurrences of 'r'

# Escape Characters
print("Hello\nWorld")  # Newline
print("Tab\tSpace")  # Tab space
print("Backslash \\ Test")  # Backslash
print("He said \"Hello\"")  # Escape quotes

# Checking Case Conditions
print("HELLO".isupper())  # True
print("hello".islower())  # True

# # Zero Padding (zfill)
# print("5".zfill(3))  # Output: '005'
# print("42".zfill(5))  # Output: '00042'

# Reversing a String Without Slicing
print("".join(reversed(p)))  # Output: 'rac'

# String Multiplication with Newlines
print(("Hello\n" * 3).strip())  # Prints 'Hello' 3 times on new lines
