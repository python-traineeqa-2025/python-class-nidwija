
n = int(input("How many inputs? "))
inputs = []
for _ in range(n):
    val = input(f"Enter value {_+1}: ")
    inputs.append(val)
print(inputs)

#
#
#
# pairs = {}
# n = int(input("How many key-value pairs? "))
# for _ in range(n):
#     key, value = input("Enter key and value separated by a space: ").split()
#     pairs[key] = value
# print(pairs)
