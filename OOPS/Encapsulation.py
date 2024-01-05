"""
Encapsulation: Here class is an example of encapsulation
as it binds all the data members and methods into a single unit.
"""


class Rectangle:  # Class creation

    def __init__(self, length, breadth):  # Constructor
        self.length = length
        self.breadth = breadth
        print(f"id of self {id(self)}")  # printing id of self to check object r1 and self are same

    def area(self):  # Method
        return self.length * self.breadth

    def perimeter(self):  # Method
        return 2 * (self.length + self.breadth)


r1 = Rectangle(10, 10)  # Creating object r1

print(f"id of r1 {id(r1)}")  # printing id of object r1 to check object r1 and self are same
print(r1.area())  # Calling method area() using object r1
