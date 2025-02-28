def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))


# def factorial_iterative(n):
#     result = 1
#     for i in range(2, n + 1):  # Start from 2
#         result *= i
#         # result=result*i
#     return result
#
# print(factorial_iterative(5))
