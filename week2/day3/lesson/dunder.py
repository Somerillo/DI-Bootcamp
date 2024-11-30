#Dunder methods: Doble UNDERscore also known as magic methods

# print(dir('Juliana'))

# __init__()
#random.shuffle() usually we need to call a method
# for dunder methods we dont need to call

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'The person is {self.name} and the birthday is {self.birthday}'

person1 = Person('Juliana', '05/02/1990')
print(person1)