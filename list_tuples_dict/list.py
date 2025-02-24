# ordered and mutable
'''
    ordered and mutable
    for grouping similar items or just items in general
'''

a = [1, 2, 3, 4, 1, 1, 1, 1]

# Accessing Elements
print(a[1])
print(len(a))

# Adding Elements
a.append(10)
print(a)

a.insert(1, 9)  # Inserts 9 at index 1
print(a)

a.insert(3, 'ram')  # Inserts 'ram' at index 3
print(a)

# Counting Occurrences
print(a.count(1))  # Number of times 1 appears (4)

# Reversing the List
a.reverse()  # Reverses the list in place
print(a)

# Sorting
b = [5, 2, 9, 1, 7]
b.sort()  # Sorts the list in ascending order
print(b)

# Using sorted() (returns a new sorted list)
d = sorted(b, reverse=True)  # Sorts in descending order
print(d)

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
print(a)

popped = a.pop()  # Removes and returns last element
print(popped)  # 7
print(a)

del a[1]  # Deletes element at index 1
print(a)