# class Music:
#     def play(self):
#         print("Music streams")
# class Games:
#     def play(self):
#         print("Match starts")

# x = Music()
# y = Games()
# x.play()
# y.play()

# class Student:
#     def __init__ (self,name,mark):
#         self.mark=mark
#         self.name=name
#     def __str__ (self):
#         return "You can't print the obj"
#     def __eq__ (self,other):
#         return self.mark==other.mark
#     def __add__ (self,other):
#         return self.mark + other.mark
# x=Student("Saathvikaa",90)
# y=Student("Raja",80)
# print(x)
# print(x==y)
# print(x+y)

from math import pi
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return  "I am a two dimensional shape."
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        super().__init__("square")
        self.length = length
    def area (self):
        return self.length**2
    def fact(self):
        return "Squares have each angle equal to 90 degree."
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius=radius
    def area(self):
        return pi*self.radius**2
    
a=Square(4)
b=Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
