# ordered and mutable
a = [1, 2, 3, 4, 1, 1, 1, 1]

# Accessing Elements
print(a[1])  # Second element (2)
print(len(a))  # Length of the list (8)

# Adding Elements
a.append(10)  # Adds 10 at the end
print(a)  # [1, 2, 3, 4, 1, 1, 1, 1, 10]

a.insert(1, 9)  # Inserts 9 at index 1
print(a)  # [1, 9, 2, 3, 4, 1, 1, 1, 1, 10]

a.insert(3, 'ram')  # Inserts 'ram' at index 3
print(a)  # [1, 9, 2, 'ram', 3, 4, 1, 1, 1, 1, 10]

# Counting Occurrences
print(a.count(1))  # Number of times 1 appears (4)

# Reversing the List
a.reverse()  # Reverses the list in place
print(a)  # Modified list in reverse order

# Sorting
b = [5, 2, 9, 1, 7]
b.sort()  # Sorts the list in ascending order
print(b)  # [1, 2, 5, 7, 9]

# Using sorted() (returns a new sorted list)
d = sorted(b, reverse=True)  # Sorts in descending order
print(d)  # [9, 7, 5, 2, 1]

# Modifying Elements
a = [1, 4, 5, 6, 7]
a[2] = 'ram'  # Replaces element at index 2
print(a)  # [1, 4, 'ram', 6, 7]

# List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Concatenation [1, 2, 3, 4, 5, 6]
print(list1 * 2)  # Repetition [1, 2, 3, 1, 2, 3]

# Checking Membership
print(4 in a)  # True
print(10 not in a)  # True

# Removing Elements
a.remove(4)  # Removes first occurrence of 4
print(a)  # [1, 'ram', 6, 7]

popped = a.pop()  # Removes and returns last element
print(popped)  # 7
print(a)  # [1, 'ram', 6]

del a[1]  # Deletes element at index 1
print(a)  # [1, 6]