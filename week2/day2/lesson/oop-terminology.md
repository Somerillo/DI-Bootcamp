OOP - Object Oriented Programing

object = instance
attributes = characterists
parameters = arguments (what we pass when creating an instance of a class)
example:
```python
class Zoo:
     def __init__(self,zoo_name):
          self.zoo_name = zoo_name #this is both: an parameter and attribute
          self.animals = [] #this is just an attribute

```

methods = function (but when it is part of a class)

Inheritance = suing attributes and methods from a class to another class (Parent or Base Class and Child or Derived Class)


Polymorphisem = using the same name of method in the Parent and Child Class but changing the output to each one of them

Encapsulation = python conventions to security measuares:
_attributename = protected
__attributename = private