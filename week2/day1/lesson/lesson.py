# OOP intro


# how to create a class

class Dog():  # siempre empieza con mayuscula, si no hay parent el () es opcional
    def __init__(self, name, color, age):  # 'self' reffers to the created object
        """
        woof woof
        """
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        """
        imprime ladrando
        """
        print(f"{self.name} esta ladrando")

    def walk(self, num_meters):
        return f"{self.name} walked {num_meters} today"

    def rename(self, new_name):
        self.name = new_name

# how to create an instance (object) of the new class we created?


shelter_dog = Dog("Rex", "black", 7)
print(type(shelter_dog))

# shelter_dog.name = "Rex"

puddle = Dog("Sowflake", "white", 3)
print(puddle.name)

# create a class called person
# use __init__() to create the following attributes: name, age, height
# create an object of this clas for yourself (the attributes)
# print your attributes


class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def presentation(self):
        """
        imprime ladrando
        """
        print(f"hola, mi nombre es {self.name}, mi edad es {
              myself.age} y mido {myself.height}m")


# this is the object:
myself = Person("Damian", 42, 1.90)
print(myself.height)

# how to change the attribute of an object after it was created
myself.age += 1
print(myself.age)

print(myself.__dict__)

shelter_dog.bark()


# create a method called presentation to print the following:
# "hola, mi nombre es {}, mi edad es {}"

myself.presentation()

print(puddle.walk(200))


class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        # Analyse the line below
        print(self)


mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")

Dog.bark(puddle)
puddle.bark()