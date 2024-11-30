#Multilevel inheritance

# class Grandpa:
#     def speak(self):
#         print('Granpa is speaking')

#     def sleep(self):
#         print('Granpa is sleeping')

# class Parent(Grandpa):
#     def speak(self):
#         print('Parent is speaking')

# class Child(Parent):
#     pass

# obj1 = Parent()
# obj1.speak()

# obj2 = Child()
# obj2.speak()



#Multiple Inheritanceclass Grandpa:

class Grandpa:
    def speak(self):
        print('Granpa is speaking')

    def sleep(self):
        print('Granpa is sleeping')

class Parent1(Grandpa):
    def speak(self):
        print('Parent1 is speaking')

    def eat(self):
        print('Parent1 is eating')


class Parent2(Grandpa):
    def speak(self):
        print('Parent2 is speaking')


class Child(Parent2, Parent1):
    pass

# obj2 = Child()
# obj2.speak()
# obj2.eat()


#the super() function
class Animal:
    def __init__(self, number_legs, sound, type = None):
        self.number_legs = number_legs
        self.sound = sound
        self.type = type

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")


class Canine(Animal):
    def __init__(self,number_legs, sound, color):
        super().__init__(number_legs, sound, 'Canine')
        self.color = color

    def fetch_ball(self):
        if self.is_trained:
            print("I am fetching balls because I am dog")
        else:
            print('This dog is not trained')


class Dog(Animal,Canine):
    def __init__(self,number_legs, sound, is_trained,color):
        super().__init__(number_legs, sound, 'dog')
        Canine.__init__(self, color)
        self.is_trained = is_trained

    def fetch_ball(self):
        if self.is_trained:
            print("I am a dog, and I love fetching balls")
        else:
            print('This dog is not trained')

    def barking(self):
        super(Dog,self).make_sound()
        

    
animal1 = Animal('dog', 4, 'Woolf')
dog1 = Dog(4, 'Woolf', True)
dog2 = Dog(4, 'Woolf', False)
print(dog1.is_trained)
dog1.fetch_ball()
dog2.fetch_ball()
dog2.barking()

