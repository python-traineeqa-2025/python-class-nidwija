
n = [10, 25, 3, 15, 50, 7]

max_num = n[0]
min_num = n[0]

# Iterate through the list to find the max and min
for num in n:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Max:", max_num)
print("Min:", min_num)
