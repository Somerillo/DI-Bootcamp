from datetime import date

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
     

    @property #getter
    def name(self):
        return self._name.title()
    
    @name.setter
    def name(self,value):
        self._name = value
        return self
        
    @property #getter
    def birthday(self):
        return self._birthday
    
    @birthday.setter #setter
    def birthday(self, value):
        if not isinstance(value, date):
            raise ValueError('birthday argument has to be a datetime object date(year, month, day)')
        self._birthday = value
        
        return self


    def lived_days(self):
        return(date.today() - self.birthday).days
    
    
    
# p1 = Person('john doe', date(1999,5,5))
# print(type(p1.name)) #title()

p2 = Person('maria gonzales', date(1980,5,2))
print(p2.name)

# create a getter and a setter for the attribute name: 
# using @property define that the name will always be printed with capital letter, even if when creating the object it was passed with lower case
# create the setter that will allow this property to be changed

