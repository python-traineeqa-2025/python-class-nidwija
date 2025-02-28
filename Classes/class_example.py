class PersonTest:
    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instancevariable
        self.age = age


    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    def ask(self):
        print("why did you call this function?")

p1 = PersonTest("ram", 26)
print(p1.introduce())
p1.ask()
