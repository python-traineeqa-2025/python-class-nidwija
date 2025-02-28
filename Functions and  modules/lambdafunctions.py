'''
lambda arguments: expression
anonymous functions
single expression function


'''

# square = lambda x: x * x
# print(square(12))
#
#
# add = lambda a, b: a + b
# print(add(4, 6))

#
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# max_val=max(10,20)
# print(max_val)
maximum = lambda x, y: x if x > y else y
print(maximum(10, 20))


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# nums = [1, 2, 3, 4]
# squares = list(map(lambda x: x * x, nums))
# print(squares)
