class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi My name is {self.name} and my age is {self.age}")

person1 = Person("omkar",24)
person1.greet()

person2 = Person("hmm",34)
person2.greet()