#OOP Intro

# How to create a class

class Dog:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        return f'{self.name} is barking'

    def walk(self,num_meters):
        return f'{self.name} walked {num_meters} meters today.'
    
    def rename(self,new_name):
        self.name = new_name
        return self.name


#How to create an instance (object) of the new class we created?

shelter_dog = Dog('Rex', 'black',7)
# print(type(shelter_dog))
# shelter_dog.name = 'Rex' #option1 creating attributes to an object

puddle = Dog('Flufy', 'white', 3)
print(puddle.walk(200))

#two different ways of calling a class method:
Dog.bark(puddle)
puddle.bark() #this one is the most common

print(shelter_dog.walk(500))

puddle.age = 5
puddle.rename('Bob')
print(puddle.name)

print(shelter_dog.name)
print(puddle.name)
shelter_dog.bark()
puddle.bark()


# create a class called Person
# use __init__() to create the following attributes: name, age, height
# create an object of this class for yourself (the attributes name, age, height og yourself )
# print all your attributes

class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def presentation(self):
        print(f'Hello, my name is {self.name}. I am {self.age} years old')

    


# # creating an object
myself = Person('Juliana', 34, 1.59)
myself.presentation()
print(myself.name, myself.age,myself.height)
print(myself.__dict__)
# print(myself)

#how to change an attribute of an object after it was created
myself.age += 1
# print(myself.age)

# created a method called presentation() to print the following:
# "Hello, my name is {}, I am {} years old"

# methods ex2

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
dell_computer.description("Mark")