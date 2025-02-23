# key-value pairs, unordered and mutable

d = {'a': 1, 'b': 2, 'c': 3}

#accessing keys and values
print(d.keys())  # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])


empty_dict = {}  # Emptydictionary
d1 = dict(name="ram", age=25, city="New York")  # Using dict()
print(d1)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing Values
print(d['a'])  # 1
print(d.get('b'))  # 2
print(d.get('z', "Not Found"))  # Returns default if key not found

# Modifying Values
d['a'] = 100  # Update value
print(d)  # {'a': 100, 'b': 2, 'c': 3}

# Adding New Key-Value Pairs
d['d'] = 4
print(d)  # {'a': 100, 'b': 2, 'c': 3, 'd': 4}

# Removing Elements
del d['b']  # Removes key 'b'
print(d)  # {'a': 100, 'c': 3, 'd': 4}

d.pop('c')  # Removes key 'c' and returns its value
print(d)  # {'a': 100, 'd': 4}

d.popitem()  # Removes the last inserted item
print(d)  # {'a': 100}

# Merging Dictionaries
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)  # Updates d1 with d2 (overwrites existing keys)
print(d1)  # {'x': 1, 'y': 3, 'z': 4}

# Dictionary Comprehension
squared = {x: x**2 for x in range(1, 6)}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Checking Key Existence
print('a' in d)  # True
print('z' in d)  # False

# Iterating Over Dictionary
for key, value in d.items():
    print(f"{key}: {value}")

# Nested Dictionaries
nested_dict = {
    'person1': {'name': 'ram', 'age': 25},
    'person2': {'name': 'shyam', 'age': 30}
}
print(nested_dict['person1']['name'])

# Copying a Dictionary
d_copy = d.copy()
print(d_copy)  # {'a': 100}

# Creating a Dictionary with Default Values
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)
print(default_dict)  # {'a': 0, 'b': 0, 'c': 0}

# Getting a Value Safely
print(d.get('a'))  # 100
print(d.get('x', 'Not Found'))
