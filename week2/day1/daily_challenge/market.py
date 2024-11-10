class Farm:
    def __init__(self, name):
        """
        Instantiate the farm class.
        name (str): the farm name
        animals (dict): a dict to store the animals, where each animal is a key
        and its amount is the value
        """
        self.name = name
        self.animals = {}

    # count default value is 1, but can accept different amounts
    def add_animal(self, animal, count=1):
        """
        updates the animal count in the farm
        animal (str): the type of animal to add
        count (int): the number of animals to add (default is 1)
        """
        if animal in self.animals:
            # if we already have the animal, we add it to the existing amount
            self.animals[animal] += count
        else:
            # if the animal does not exist, add it with the specified count
            self.animals[animal] = count

    def get_info(self):
        """
        Returns a string with the farm name, animals and count, and message
        """
        output = f"{self.name}`s farm\n\n"
        # adds the dictionary items to the string line by line
        for animal, count in self.animals.items():
            output += f"{animal} : {count}\n"
        # adds the las message
        output += "\n    E-I-E-I-0!"
        # finally return output, without this last line we just get None
        return output

    def get_animal_types(self):
        """
        return a sorted list of all the animal types (names) in the farm
        """
        return sorted(self.animals.keys())

    def get_short_info(self):
        """
        return the following string: ``McDonald`s farm has cows, goats and sheeps``.
        """
        animal_types = self.get_animal_types()
        list_animal_types = []
        # check the key `animal` if its singular or plural
        for animal in animal_types:
            if self.animals[animal] == 1:
                list_animal_types.append(animal)
            else:
                list_animal_types.append(animal + "s")
        string = f"McDonald`s farm has {
            ", ".join(list_animal_types[:-1])} and {list_animal_types[-1]}."
        return string


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

# expand the farm:
print()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
ascii_art = """
██╗    ██╗  ██╗ █████╗ ████████╗███████╗     ██████╗  ██████╗ ██████╗ 
██║    ██║  ██║██╔══██╗╚══██╔══╝██╔════╝    ██╔═══██╗██╔═══██╗██╔══██╗
██║    ███████║███████║   ██║   █████╗      ██║   ██║██║   ██║██████╔╝
██║    ██╔══██║██╔══██║   ██║   ██╔══╝      ██║   ██║██║   ██║██╔═══╝ 
██║    ██║  ██║██║  ██║   ██║   ███████╗    ╚██████╔╝╚██████╔╝██║     
╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝  ╚═════╝ ╚═╝     
"""
print(ascii_art)