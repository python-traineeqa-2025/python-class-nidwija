# Take a list of numbers as input
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Initialize an empty list to store the squares of even numbers
squared_evens = []

# Iterate through the list
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        squared_evens.append(num ** 2)  # Add the square of the even number to the list

# Print the result
print("Squares of even numbers:", squared_evens)


