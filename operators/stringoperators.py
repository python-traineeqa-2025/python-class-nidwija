# Basic String Operations
p = 'car'
r = 'race'

print(p + r)  # Concatenation
print(p * 4)  # Repetition
print(p[1])  # Indexing
print(r[1:3])  # Slicing [start:end]
print(p[::-1])  # Reverse string


print(p.upper())  # Uppercase
print(p.lower())  # Lowercase
print(p.title())  # Title Case

# trim and replace
a = ' hello '
print(a.strip())  # Remove spaces from both ends
print(r.replace('r', 'f'))  # Replace characters

# split/join
b = 'hello my name'
print(b.split(' '))  # Split into a list
o = ['hello', 'hi']
print(','.join(o))  # Join with a separator
