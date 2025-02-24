# Basic Arithmetic Operations
a = 10
b = 3

print(a + b)  # Addition (10 + 3 = 13)
print(a - b)  # Subtraction (10 - 3 = 7)
print(a * b)  # Multiplication (10 * 3 = 30)
print(a / b)  # Division (10 / 3 = 3.3333)
print(a // b)  # Floor Division (10 // 3 = 3) - removes decimal part
print(a % b)  # Modulus (10 % 3 = 1) - remainder
print(a ** b)  # Exponentiation (10^3 = 1000)

# comparison
print(a > b)  # Greater than (True)
print(a < b)  # Less than (False)
print(a >= b)  # Greater than or equal to (True)
print(a <= b)  # Less than or equal to (False)
print(a == b)  # Equality check (False)
print(a != b)  # Not equal check (True)

# Bitwise
print(a & b)  # AND (10 & 3 = 2)
print(a | b)  # OR (10 | 3 = 11)
print(a ^ b)  # XOR (10 ^ 3 = 9)
print(~a)  # Bitwise NOT (~10 = -11)
print(a << 1)  # Left shift (10 << 1 = 20) - Multiply by 2
print(a >> 1)  # Right shift (10 >> 1 = 5) - Divide by 2

# Typecasting
c = "15"
print(int(c) + 5)  # Convert string to integer and add (15 + 5 = 20)
print(float(a))  # Convert integer to float (10.0)
print(str(a))  # Convert integer to string ('10')
