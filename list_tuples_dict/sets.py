# unordered and mutable, but elements must be unique
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# Creating a Set
empty_set = set()  # This creates an empty set (not {})
set_from_list = set([1, 2, 3, 1, 2, 4])  # Removes duplicates
print(set_from_list)  # {1, 2, 3, 4}

# Accessing Elements(not possible directly as sets are unordered)
for item in s1:
    print(item)  # Iterating over set

# Adding Elements
s1.add(10)  # Adds 10 to the set
print(s1)  # {1, 2, 3, 4, 5, 10}

# Removing Elements
s1.remove(3)  # Removes 3 (Error if not present)
print(s1)  # {1, 2, 4, 5, 10}

s1.discard(5)  # Removes 5 (No error if not present)
print(s1)  # {1, 2, 4, 10}

popped_element = s1.pop()  # Removes and returns an arbitrary element
print(popped_element)
print(s1)

s1.clear()  # Removes all elements from the set
print(s1)  # set()

# Set Operations
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)  # Union: {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2))  # Alternative for union

print(s1 & s2)  # Intersection: {3, 4, 5}
print(s1.intersection(s2))  # Alternative for intersection

print(s1 - s2)  # Difference: {1, 2}
print(s1.difference(s2))  # Alternative for difference

print(s1 ^ s2)  # Symmetric Difference: {1, 2, 6, 7}
print(s1.symmetric_difference(s2))  # Alternative for symmetric difference

# Checking Membership
print(2 in s1)  # True
print(10 not in s1)  # True

# Set Length
print(len(s1))  # 5

# Subset and Superset Checks
s3 = {1, 2}
print(s3.issubset(s1))  # True (s3 is subset of s1)
print(s1.issuperset(s3))  # True (s1 is superset of s3)

# Copying a Set
s4 = s1.copy()
print(s4)  # {1, 2, 3, 4, 5}

# Frozen Sets (Immutable Sets)
fset = frozenset([1, 2, 3, 4])
print(fset)  # frozenset({1, 2, 3, 4})

# Uncommenting the below line will throw an error since frozen sets are immutable
# fset.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
