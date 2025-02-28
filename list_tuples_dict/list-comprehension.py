'''
new_list = [expression for item in iterable if condition]

'''


# squares = []
# for x in range(5):
#     squares.append(x**2)
# print(squares)
#
# # List Comprehension
# squares = [x**2 for x in range(5)]
# print(squares)


evens = [x**2 for x in range(10) if x % 2 == 0]
print(evens)

evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x**2)
print(evens)
