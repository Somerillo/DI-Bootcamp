## --------------------------------------- Exercise 1: Cats --------------------------------------- ##
# # Instructions

# # Using this class

# # class Cat:
# #     def __init__(self, cat_name, cat_age):
# #         self.name = cat_name
# #         self.age = cat_age

# #     Instantiate three Cat objects using the code provided above.
# #     Outside of the class, create a function that finds the oldest cat and returns the cat.
# #     Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age


# cat_1 = Cat("poncho", 5)
# cat_2 = Cat("luna", 32)
# cat_3 = Cat("bato", 12)


# def cat_older(*cats):
#     oldest_cat = cats[0]
#     for cat in cats[1:]:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return oldest_cat


# oldest_cat = cat_older(cat_1, cat_2, cat_3)

# print(f"The oldest cat is < {oldest_cat.name} >, and is < {
#       oldest_cat.age} > years old.")


## --------------------------------------- Exercise 2 : Dogs --------------------------------------- ##
# # Instructions

# #     Create a class called Dog.
# #     In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes,
# # which values are the parameters.
# #     Create a method called bark that prints the following string “<dog_name> goes woof!”.
# #     Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# #     Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# #     Print the details of his dog (ie. name and height) and call the methods bark and jump.
# #     Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# #     Print the details of her dog (ie. name and height) and call the methods bark and jump.
# #     Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


# class Dog:
#     """
#     a class called Dog

#     attributes:
#         name (str): The name of the dog.
#         height (float): The height of the dog in centimeters.
#     """

#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height

#     def bark(self):
#         print(f"< {self.name} > goes woof!")

#     def jump(self):
#         print(f"< {self.name} > jumps < {self.height**2} > cm high!”.")


# davids_dog = Dog("Rex", 50)
# print(f"davis dog is {davids_dog.name}, its height is {davids_dog.height} cm")
# davids_dog.bark()
# davids_dog.jump()

# print()

# sarahs_dog = Dog("Teacup", 20)
# print(f"sarahs dog is {sarahs_dog.name}, its height is {sarahs_dog.height} cm")
# sarahs_dog.bark()
# sarahs_dog.jump()

# print()

# if davids_dog.height > sarahs_dog.height:
#     print(f"the biggest dog is {davids_dog.name}")
# elif davids_dog.height < sarahs_dog.height:
#     print(f"the biggest dog is {sarahs_dog.name}")
# else:
#     print("both dogs have same height")


## --------------------------------------- Exercise 3 : Who’s the song producer? --------------------------------------- ##
# # Instructions

# #     Define a class called Song, it will show the lyrics of a song.
# #     Its __init__() method should have two arguments: self and lyrics (a list).
# #     Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

# #     Create an object, for example:

# #     stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# #     Then, call the sing_me_a_song method. The output should be:

# #     There’s a lady who's sure
# #     all that glitters is gold
# #     and she’s buying a stairway to heaven

# class Song:
#     """
#     it will show the lyrics of a song
#     """

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for i in self.lyrics:
#             print(i)


# stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
#                 "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()


## --------------------------------------- Exercise 4 : Afternoon at the Zoo --------------------------------------- ##
# # Instructions

# #     Create a class called Zoo.
# #     In this class create a method __init__ that takes one parameter: zoo_name.
# #     It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# #     Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# #     Create a method called get_animals that prints all the animals of the zoo.
# #     Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

# #     Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# #     Example

# #     {
# #         1: "Ape",
# #         2: ["Baboon", "Bear"],
# #         3: ['Cat', 'Cougar'],
# #         4: ['Eel', 'Emu']
# #     }


# #     Create a method called get_groups that prints the animal/animals inside each group.
# #     Create an object called ramat_gan_safari and call all the methods.
# #     Tip: The zookeeper is the one who will use this class.
# #     Example

# #     Which animal should we add to the zoo --> Giraffe
# #     x.add_animal(Giraffe)


# class Zoo:  # Create a class called Zoo.
#     """
#     Afternoon at the Zoo
#     """

#     def __init__(self, zoo_name):
#         self.name = zoo_name
#         self.animals = []

#     def add_animal(self, new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#             print(f"added: {new_animal}")
#         else:
#             print(f"{new_animal} already in the zoo")

#     def get_animals(self):
#         print(self.animals)
#         return self.animals

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#             print(f"removed: {animal_sold}")
#         else:
#             print(f"{animal_sold} not in the list")

#     def sort_animals(self):
#         animals_sorted = sorted(self.animals)  # sort the list
#         grouped_animals = {}  # isntantiate dictionary
#         group_index = 1  # instantiate index

#         for animal in animals_sorted:
#             first_letter = animal[0]
#             if group_index not in grouped_animals:
#                 grouped_animals[group_index] = [animal]
#             elif grouped_animals[group_index][0][0] == first_letter:
#                 grouped_animals[group_index].append(animal)
#             else:
#                 group_index += 1
#                 grouped_animals[group_index] = [animal]

#         return grouped_animals

#     def get_groups(self):
#         """
#         prints the animal/animals inside each group.
#         """
#         grouped_animals = self.sort_animals()  # get the sorted groups
#         for group_index, animals in grouped_animals.items():
#             print(f"group {group_index}: {animals}")


# ramat_gan_safari = Zoo("ramat gan safari")


# list_animals = ["Ape", "Ape", "Baboon", "Bear",
#                 "Cat", "Cougar", "Eel", "Emu", "Emu"]

# for animal in list_animals:
#     ramat_gan_safari.add_animal(animal)


# print()
# ramat_gan_safari.get_animals()

# print()
# ramat_gan_safari.sell_animal("Koala")
# ramat_gan_safari.sell_animal("Ape")

# print()
# ramat_gan_safari.add_animal("Ape")
# print(ramat_gan_safari.sort_animals())

# print()
# ramat_gan_safari.get_groups()
