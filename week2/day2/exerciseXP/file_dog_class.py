import random


class Dog:
    def __init__(self, name, age, weight):
        self.name = name  # ATTRIBUTE: stores the dog`s name
        self.age = age  # ATTRIBUTE: stores the dog`s age
        self.weight = weight  # ATTRIBUTE: stores the dog`s weight !!!!!!!!!!!!

    def bark(self):
        """
        returns a string which states: “<dog_name> is barking”.
        """
        return f"{self.name} is barking"

    def run_speed(self):  # METHOD: calculates and returns the dog's running speed !!!!!!!!!!!
        """
        returns the dogs running speed (weight/age*10).
        """
        return self.weight / self.age*10  # uses attributes to perform a calculation !!!!!!!!

    def fight(self, other_dog):
        """
        takes a parameter which value is another Dog instance, called other_dog.
        This method returns a string stating which dog won the fight.
        """
        # calculate strength: run_speed (method call) times weight (attribute access)
        # self.run_speed() has () because it's a method that needs to be executed to get the speed value
        # self.weight doesn't have () because it's an attribute, directly accessing the stored weight value
        self_strength = self.run_speed() * self.weight
        other_dog_strength = other_dog.run_speed() * other_dog.weight
        if self_strength > other_dog_strength:
            # name is an attribute and bc of that doesnt have ()
            return f"{self.name} won against {other_dog.name}"
        elif self_strength < other_dog_strength:
            return f"{self.name} lost against {other_dog.name}"
        else:
            return f"the fight was a tie"


# dog1 = Dog("dog1", 9, 40)
# dog2 = Dog("dog2", 8, 24)
# dog3 = Dog("dog3", 12, 30)

# print(dog1.fight(dog2))
# print(dog2.fight(dog3))
# print(dog3.fight(dog1))


# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# -    train: prints the output of bark and switches the trained boolean to True

# -    play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string:
#  “dog_names all play together”.

# -    do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#         “dog_name does a barrel roll”.
#         “dog_name stands on his back legs”.
#         “dog_name shakes your hand”.
#         “dog_name plays dead”.

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):

        # When we create a subclass, it inherits methods and attributes from its parent class.
        # However, the __init__ method (constructor) of the parent class is not automatically
        # called when you create an INSTANCE of the SUBCLASS.
        # This is why we often use super().__init__() in the subclass's __init__ method.

        # call the parent class's __init__ method
        super().__init__(name, age, weight)
        # add the trained attribute
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # if we didn't use [], it would result in an error because we can't directly
        # concatenate a string (self.name) with a list (list(args)).
        dog_names = ", ".join([self.name] + list(args))
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained")


# dog1 = PetDog("dog1", 17, 70)
# dog2 = PetDog("dog2", 17, 70, trained=True)
# dog3 = PetDog("dog3", 17, 70, trained=False)
# dog1.do_a_trick()
# dog2.do_a_trick()
# dog3.do_a_trick()