"""class Person:
    #class attributes
    address = 'no information'

    # constructor (constructive)
    def __init__(self,name,year):
        # object attributes
        self.name = name
        self.year = year

    #instance methods
    def intro(self):
        print('hello there. I am '+ self.name)
    
    def calculateAge(self):
        return 2022- self.year



p1 = Person(name = 'cansu',year =1997 )
p2 = Person('Merthan', 1996)

p1.name='CANSU'

print(f'name : {p1.name} year : {p1.year} my age {p1.calculateAge()}')
print(f'name : {p2.name} year : {p2.year}')

"""

class Circle:
    #class attribu    
    pi = 3.15

    def __init__(self,radious=1):
        self.radious=radious
    
    def perimeter(self):
        return 2 * self.pi * self.radious

    def area(self):
        return  self.pi * (self.radious**2)

c1 = Circle()
c2 = Circle(5)

print(f'c1 area : {c1.area()} perimeter : {c1.perimeter()}')
print(f'c2 area : {c2.area()} perimeter : {c2.perimeter()}')






