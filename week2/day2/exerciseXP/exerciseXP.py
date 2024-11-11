## ------------------------------------------------- Exercise 1 : Pets ------------------------------------------------- ##
# # Instructions

# # Using this code:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# #     Create another cat breed named Siamese which inherits from the Cat class.
# class Siamese(Cat):
#     pass


# # Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# all_cats = [Bengal("bengal_name", 32), Chartreux(
#     "charteaux_name", 25), Siamese("siamese_name", 15)]

# # Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class,
# # and pass the variable all_cats to the new instance.
# sara_pets = Pets(all_cats)

# # Take all the cats for a walk, use the walk method.
# sara_pets.walk()

# # ------------------------------------------------- Exercise 2 : Dogs ------------------------------------------------- ##
# # Instructions

# # Create a class called Dog with the following attributes name, age, weight.
# # Implement the following methods in the Dog class:
# # - bark: returns a string which states: “<dog_name> is barking”.
# # - run_speed: returns the dogs running speed (weight/age*10).
# # - fight : takes a parameter which value is another Dog instance, called other_dog.
# #   This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# #     Create 3 dogs and run them through your class.

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name # ATTRIBUTE: stores the dog`s name
#         self.age = age  # ATTRIBUTE: stores the dog`s age
#         self.weight = weight # ATTRIBUTE: stores the dog`s weight !!!!!!!!!!!!

#     def bark(self):
#         """
#         returns a string which states: “<dog_name> is barking”.
#         """
#         return f"{self.name} is barking"

#     def run_speed(self): # METHOD: calculates and returns the dog's running speed !!!!!!!!!!!
#         """
#         returns the dogs running speed (weight/age*10).
#         """
#         return self.weight / self.age*10 # uses attributes to perform a calculation !!!!!!!!

#     def fight(self, other_dog):
#         """
#         takes a parameter which value is another Dog instance, called other_dog.
#         This method returns a string stating which dog won the fight.
#         """
#         # calculate strength: run_speed (method call) times weight (attribute access)
#         # self.run_speed() has () because it's a method that needs to be executed to get the speed value
#         # self.weight doesn't have () because it's an attribute, directly accessing the stored weight value
#         self_strength = self.run_speed() * self.weight
#         other_dog_strength = other_dog.run_speed() * other_dog.weight
#         if self_strength > other_dog_strength:
#             return f"{self.name} won against {other_dog.name}" # name is an attribute and bc of that doesnt have ()
#         elif self_strength < other_dog_strength:
#             return f"{self.name} lost against {other_dog.name}"
#         else:
#             return f"the fight was a tie"


# dog1 = Dog("dog1", 9, 40)
# dog2 = Dog("dog2", 8, 24)
# dog3 = Dog("dog3", 12, 30)

# print(dog1.fight(dog2))
# print(dog2.fight(dog3))
# print(dog3.fight(dog1))


# # ------------------------------------------------- Exercise 3 : Dogs Domesticated ------------------------------------------------- ##
# # Create a new python file and import your Dog class from the previous exercise.
# # In the new python file, create a class named PetDog that inherits from Dog.
# # Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# # Add the following methods:
# # -    train: prints the output of bark and switches the trained boolean to True

# # -    play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# # -    do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# #         “dog_name does a barrel roll”.
# #         “dog_name stands on his back legs”.
# #         “dog_name shakes your hand”.
# #         “dog_name plays dead”.

# from file_dog_class import Dog, PetDog

# dog1 = PetDog("dog1", 17, 70)  # trained default False
# dog2 = PetDog("dog2", 17, 70, trained=True)
# dog3 = PetDog("dog3", 17, 70, trained=False)

# # trained set to True
# # CAUTION!!!! it uses [self.name] + list(args) !!!!!!!!!!!!!!
# dog1.train()

# dog1.play(dog2.name, dog3.name)
# dog1.play("julian", "lula")

# dog1.do_a_trick()
# dog2.do_a_trick()
# dog3.do_a_trick()

# # ------------------------------------------------- Exercise 4 : Family ------------------------------------------------- ##
# # Create a class called Family and implement the following attributes:
# # -    members: list of dictionaries
# # -    last_name : (string)

# # Implement the following methods:
# # -    born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# # -    is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# # -    family_presentation: a method that prints the family’s last name and all the members’ details.

# class Family:
#     """
#     Creates a class called Family and implement the following attributes:
#     members: list of dictionaries
#     last_name : (string)
#     """

#     def __init__(self, last_name, members):
#         self.members = members
#         self.last_name = last_name

#     def born(self, **kwargs):
#         """
#         adds a child to the members list (use **kwargs)
#         """
#         self.members.append(kwargs)
#         print(f"a message congratulating the family < {self.last_name} > on the birth of < {kwargs["name"]} >")

#     def is_18(self, name):
#         """
#         takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
#         """
#         for member in self.members:
#             if member["name"] == name:
#                 if member["age"] >= 18:
#                     return True
#             return False

#     def family_presentation(self):
#         """
#         a method that prints the family`s last name and all the members` details.
#         """
#         print(f"family {self.last_name}:")
#         for member in self.members:
#             print(f"name: {member["name"]}, age: {member["age"]}, gender: {member["gender"]}, is child: {member["is_child"]}")


# # Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

# #     [
# #         {'name':'Michael','age':35,'gender':'Male','is_child':False},
# #         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# #     ]

# family = Family(last_name="Smith", members=[
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ])

# family.born(name='baby_name', age=0, gender='Male', is_child=True)
# print(family.is_18('Michael'))
# print(family.is_18('baby_name'))
# family.family_presentation()

# # # ------------------------------------------------- Exercise 5 : TheIncredibles Family ------------------------------------------------- ##
# # Create a class called TheIncredibles. This class should inherit from the Family class:
# # This is no random family they are an incredible family, therefore the members attributes,
# # will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

# # Add a method called use_power, this method should print the power of a member only if they are over 18 years old.
# # If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# # Add a method called incredible_presentation which :
# # -    Print a sentence like “*Here is our powerful family **”
# # -    Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)

# print("-----------------------------------------------------------------------")

# class TheIncredibles(Family):
#     """
#     This class inherit from the Family class \n
#     the members attributes, are a list of dictionaries \n
#     containing the additional keys : power and incredible_name
#     """

#     # up here ALL the attributes, including the new ones
#     def __init__(self, last_name, members):
#         super().__init__(last_name, members)

#     def use_power(self, name):
#         for member in self.members:
#             if member["name"] == name:
#                 if member["age"] >= 18:
#                     print(f"{member["name"]} uses {member["power"]}")
#                     return
#                 raise Exception(f"{name} is a minor")

#     def incredible_presentation(self):
#         print("*Here is our powerful family **")
#         super().family_presentation() # calls the family_presentation from the parental class


# # Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

# # [
# #     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
# #     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# # ]

# family_incred = TheIncredibles(last_name="The Incredibles", members=[
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
#         'power': 'fly', 'incredible_name': 'MikeFly'},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
#      'power': 'read minds', 'incredible_name': 'SuperWoman'}
# ])

# # Call the incredible_presentation method.
# family_incred.incredible_presentation()

# # Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# family_incred.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

# # Call the incredible_presentation method again.
# family_incred.incredible_presentation()

# family_incred.use_power('Michael')
# try:
#     family_incred.use_power('Jack')
# except Exception as e:
#     print(e)

# ascii_art = """
# ██╗    ██████╗ ███████╗███████╗██████╗ ██╗███████╗███████╗     ██████╗  ██████╗ ██████╗ 
# ██║    ██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔════╝██╔════╝    ██╔═══██╗██╔═══██╗██╔══██╗
# ██║    ██║  ██║█████╗  ███████╗██████╔╝██║███████╗█████╗      ██║   ██║██║   ██║██████╔╝
# ██║    ██║  ██║██╔══╝  ╚════██║██╔═══╝ ██║╚════██║██╔══╝      ██║   ██║██║   ██║██╔═══╝ 
# ██║    ██████╔╝███████╗███████║██║     ██║███████║███████╗    ╚██████╔╝╚██████╔╝██║     
# ╚═╝    ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝  ╚═════╝ ╚═╝     
# """
# print(ascii_art)