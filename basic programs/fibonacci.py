n = int(input("Enter the number of Fibonacci terms to generate: "))

fib_series = [0, 1]
while len(fib_series) < n:
    fib_series.append(fib_series[-1] + fib_series[-2])
print("Fibonacci Series:", fib_series)
