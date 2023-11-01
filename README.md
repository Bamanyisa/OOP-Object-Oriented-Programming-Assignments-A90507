Question 5

Describe how multilevel, Hybrid and Hierarchical inheritance work.

a.	Multilevel Inheritance: In multilevel inheritance, a class derives from another class, which in turn derives from another class. It forms a chain of classes. For example, Class A -> Class B -> Class C.

Example
<pre>
```python

class Grandparent:
    def method1(self):
        pass

class Parent(Grandparent):
    def method2(self):
        pass

class Child(Parent):
    def method3(self):
        pass

```
</pre>

b.	Hybrid Inheritance: Hybrid inheritance is a combination of different types of inheritance, such as multiple, single, and multilevel inheritance within a program.

Example
<pre>
```python

class A:

class B(A):
    

class C(A):

class D(B, C):

```
</pre>


c.	Hierarchical Inheritance: Hierarchical inheritance is a type of inheritance where multiple classes inherit from a single base class. For example, Class A -> Class B, Class C, Class D.

Example
<pre>
```python

class Animal:

    def speak(self):
        pass

class Dog(Animal):
    
    def speak(self):
        print("Woof")

class Cat(Animal):
    
    def speak(self):
        print("Meow")

```
</pre>
