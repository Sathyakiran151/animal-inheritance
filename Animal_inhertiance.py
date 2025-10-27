'''Create a base class Animal with properties like name, age, and sound().

Derive subclasses like Dog, Cat, Cow, each overriding sound().'''
class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sound(self):
        print("animal makes the sound")
class Dog(Animal):
    def sound(self):
        print("bow bow")
class Cat(Animal):
    def sound(self):
        print("meow meow")
class Cow(Animal):
    def sound(self):
        print("amba amba")
dog = Dog("tyson",3)
cat= Cat("tommy",4)
cow = Cow("chinni",5)
dog.sound()
cat.sound()
cow.sound()
        
        
    