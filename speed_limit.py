'''4. Vehicle Speed System

Concept: Method overriding using inheritance.

Description:
Create a base class Vehicle with a max_speed() method.
Subclasses → Car, Bike, Truck.
Each subclass returns its unique top speed.'''

class vehicle():
    def __init__(self,speed):
        self.speed=speed
    def max_speed(self):
        print(f"The  maximum  speed limit of vehicle is {self.speed}")
class bike(vehicle):
    def __init__(self,speed,speed1):
        self.speed=speed
        self.speed1=speed1
    def max_speed(self):
        print(f"the speed limit of bike in urban area :{self.speed}")
        
        print(f"the speed limit of bike in Highway :{self.speed1}")
class car(vehicle):
        def __init__(self,speed,speed1):
            self.speed=speed
            self.speed1=speed1
            
        def max_speed(self):
            print(f"the speed of car in city roads :{self.speed}")
            print(f"the speed linit of car in highways :{self.speed1}")

class truck(vehicle):
    def __init__(self,speed,speed1):
        self.speed=speed
        self.speed1=speed1
    def max_speed(self):
        print(f"the speed limit  of truck in urban area :{self.speed}")
        print(f"the speed limit of truck in highways :{self.speed1}")
       
a=vehicle(100)
b=bike(50,80)
c=car(50,100)
d=truck(30,80)

a.max_speed()
b.max_speed()
c.max_speed()
d.max_speed()

        