"""
Task 2
Write a python program that creates a class called Person which contains Name, Sex and Profession as states (attributes) and working, study and leave as its behaviours. 
Demonstrate with examples the use of classes and objects.

"""
class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def working(self):
        return f"{self.name} is working."

    def study(self):
        return f"{self.name} is studying."

    def leave(self):
        return f"{self.name} is on leave."


person1 = Person("Alice", "Female", "Engineer")
person2 = Person("Bob", "Male", "Teacher")

print(person1.working())
print(person2.study())
print(person1.leave())    
print(person2.leave())

