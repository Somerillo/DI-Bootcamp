# class Grampa:
#     def speak(self):
#         print("grampa is speaking")

# class Parent:
#     def speak(self):
#         print("parent is speaking")


# class Child(Parent):
#     pass

# obj1 = Parent()
# obj1.speak()

# obj2 = Child()
# obj2.speak()


# -------------------------------------------------------------------------------

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# # output: 4 x self diam??
# print(nc.diameter)


# ------------------------------------------------------------------------

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")


# class Dog(Animal):
#     def __init__(self, number_legs, sound, is_trained):
#         super().__init__("Dog", number_legs, sound)
#         self.is_trained = is_trained

#     def fetch_ball(self):
#         print("I am a dog, and I love fetching balls")

#     def make_sound(self):
#         print("I am an DOGGG !!! WOUAFFF!!")

#     def barking(self):
#         super(Dog, self).make_sound() # same action but not same name for the parent action


# ## VER class Canine!!!!!!!!!!!!!!!!!!!!1

# rex = Dog('dog', 4, "Wouaf")
# rex.make_sound()
# # >> I am an DOGGG !!! WOUAFFF!!
# lol = Dog(4, "bark", False)
# lol.fetch_ball()
# lol.barking() ## reemplazo el comando parent!!!!


# --------------------------------------------------------- # ENCAPSULATION:

# # Try to recreate the class explained below:

# # We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

# # We can create a class called BlockedDoor that inherits from the base class Door.

# # We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions,
# # which simply raises an Error that a blocked door cannot be opened or closed.

# class Door:
#     def __init__(self, is_opened=True):
#         self.is_opened = is_opened

#     def open_door(self):
#         if self.is_opened:
#             print("the door was already opened")
#         else:
#             print("the door is now opened")

#     def close_door(self):
#         if not self.is_opened:
#             print("the door was already closed")
#         else:
#             print("the door is now closed")
#             self.is_opened = False


# class BlockedDoor(Door):
#     def open_door(self):
#         raise Exception("blocked door cant be opened")

#     def close_door(self):
#         raise Exception("blocked door cant be closed")


# door1 = Door()
# door2 = BlockedDoor()

# door1.close_door()
# print(door1.is_opened)

# door2.close_door()


## -------------------------------------------------------------------------------------------
# Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious string inside the list.

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def sumatoria(lis = my_list):
    try:
        suma = sum(lis)
    except:
        print("not all numbers")

sumatoria()