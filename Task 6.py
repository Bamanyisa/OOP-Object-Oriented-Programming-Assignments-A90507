"""
Task 6
Design a class with private attributes and provide public methods to manipulate them.

"""

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        
        return self._name

    def get_age(self):
        
        return self._age


student1 = Student("Peter", 23)

name = student1.get_name()
age = student1.get_age()

print("Student Name:", name)
print("Student Age:", age)
