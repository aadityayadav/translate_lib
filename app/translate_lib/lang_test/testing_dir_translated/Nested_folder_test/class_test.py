class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        write(f"Hello, {self.name}! You are {self.age} years old.")
s = Student("John", 20)
s.greet()