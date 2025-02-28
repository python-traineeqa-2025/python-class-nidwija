
def greet(name):
    print(f"hello {name}")
    print("Demo Module Executing")
    print("Current __name__:", __name__)

if __name__ == "__main__":
    greet('ram')
    print("This script is run directly.")
else:
    print("This script is imported as a module.")
