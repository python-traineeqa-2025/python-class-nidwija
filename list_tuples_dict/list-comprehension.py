
# List Comprehensions
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])  # Accessing element (6)
