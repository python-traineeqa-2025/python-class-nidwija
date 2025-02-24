'''
lambda arguments: expression

'''

square = lambda x: x * x
print(square(12))


add = lambda a, b: a + b
print(add(4, 6))


maximum = lambda x, y: x if x > y else y
print(maximum(10, 20))


students = [("A", 25), ("B", 22), ("C", 23)]
students.sort(key=lambda x: x[1])
print(students)

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)
