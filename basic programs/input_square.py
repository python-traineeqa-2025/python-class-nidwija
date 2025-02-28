# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
user_input = (input("Enter space-separated values: ").split())
numbers = user_input

# for x in user_input.split():
#     numbers.append(int(x))

squared_evens = []

for num in numbers:
    if int(num) % 2 == 0:  # Check if the number is even
        squared_evens.append(int(num) ** 2)  # Add the square of the even number to the list

print("Squares of even numbers:", squared_evens)


