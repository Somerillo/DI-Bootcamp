from modules import Animal, addition
import random as rand
import pandas as pd
import pygame

class Cat(Animal):
    pass

my_cat = Cat()
print(my_cat.walk())

print(addition(4,8))

print(rand.randint(1,10))
