class Animal:
    def walk(self):
        return f'this animal is walking'


#some function (not method)
def addition(a,b):
    return a+b
    
if __name__ == "__main__":
    
    animal = Animal()
    print(animal.walk())