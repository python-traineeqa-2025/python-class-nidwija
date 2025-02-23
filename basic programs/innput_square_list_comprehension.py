
# Take a list of numbers as input
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Iterate through the list and square even numbers
squared_evens = [x**2 for x in numbers if x % 2 == 0]

# Print the result
print("Squares of even numbers:", squared_evens)
