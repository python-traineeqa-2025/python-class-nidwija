x=3
print(x)
def outer():
    x = 5
    print(f"outer variable but before inner: {x}")
    def inner():
        nonlocal x
        x = 10
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print(x)


