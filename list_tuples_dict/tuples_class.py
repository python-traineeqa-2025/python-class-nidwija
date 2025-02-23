# immutable
a = (1, 2)
b = {1, 3, 53}  # This is a set, not a tuple
t = [1, 2, 3, 4, 1, 1, 1, 1]

# Converting list to set (removes duplicates)
print(set(t))  # {1, 2, 3, 4}

# Creating Tuples
t1 = (1, 2, 3, 4, 5)
t2 = ("hello", 3.5, True)

# Accessing Elements
print(t1[0])  # First element (1)
print(t1[-1])  # Last element (5)
print(t1[1:4])  # Slicing (2, 3, 4)
print(t1[::-1])  # Reverse tuple (5, 4, 3, 2, 1)

# Tuple Operations
print(t1 + t2)  # Concatenation (creates a new tuple)
print(t1 * 2)  # Repetition (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking Membership
print(3 in t1)  # True
print(10 not in t1)  # True

# Tuple Length
print(len(t1))  # 5

# Tuple Methods
t3 = (1, 2, 3, 1, 1, 4, 5)

print(t3.count(1))  # Count occurrences of 1 (3)
print(t3.index(3))  # Index of first occurrence of 3 (2)

# Tuples with One Element (Must include a comma)
single_element_tuple = (5,)
print(type(single_element_tuple))  # <class 'tuple'>

# Tuple Packing & Unpacking
packed_tuple = 10, 20, 30  # Packing
print(packed_tuple)  # (10, 20, 30)

a, b, c = packed_tuple  # Unpacking
print(a, b, c)  # 10 20 30

# Converting List to Tuple
list1 = [10, 20, 30]
tuple_from_list = tuple(list1)
print(tuple_from_list)  # (10, 20, 30)

# Converting Tuple to List
tuple1 = (10, 20, 30)
list_from_tuple = list(tuple1)
print(list_from_tuple)  # [10, 20, 30]

# Nested Tuples
nested_tuple = ((1, 2, 3), (4, 5, 6))
print(nested_tuple[1][2])  # Accessing element (6)

# Tuple Immutability Test
# t1[0] = 10  # TypeError: 'tuple' object does not support item assignment
