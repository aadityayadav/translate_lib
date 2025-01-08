
वर्ग Student:
    परिभाषित __init__(self, name, age):
        self.name = name
        self.age = age
        
    परिभाषित greet(self):
        लिखो(f"Hello, {self.name}! You are {self.age} years old.")
        
s = Student("John", 20)
s.greet()
