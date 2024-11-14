# sintax
lambda n,power: n ** power

# tambien podemos nobrar una variable con la lambda
to_power = lambda n,power: n ** power
print(to_power(4,2))


numbers = [x for x in range(1,8)]

squared_numbers = map(lambda n: n**2, numbers)
# squared_numbers = lambda n: n**2, numbers # asi tampoco funca
print(squared_numbers) # asco
print(list(squared_numbers))

# in context: applying to a dataset
import pandas as pd




# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters:
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# discover if the len(name) <= 4
# say hello just for those that len(name) <= 4
# use map() and filter()

applicabel_names = list(filter(lambda name: len(name) <= 4, people))
print(applicabel_names)


say_hello = list(map(lambda name: f"hello {name}", applicabel_names)) # no tengo la mas puta idea de lo que estoy haciendo!!!!!!!!!!!!!!!
print(say_hello)