class Animal:
    def __init__(self, number_legs, sound, type = None):
        self.number_legs = number_legs
        self.sound = sound
        self.type = type

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

def my_func(a,b):
    return a+b