#FUNCTIONS
#Syntax

# def say_hello():
#     print('Hello Python')

# #calling the function
# say_hello()


#argument
# def say_hello(greeting):
#     name = input('What`s your name')
#     print(greeting, name)


# say_hello('Shalom') 

def say_hello(name= 'John Doe', language = 'HE'):
    if language == "HE":
        print(f'Shalom, {name}')
    elif language == "PT":
        print(f'Ola, {name}')
    elif language == "RU":
        print(f'Priviet, {name}')
    elif language == "FR":
        print(f'Bonjour, {name}')
    else:
        print(f'{language} is not supported')

say_hello('Arielle', 'FR')

#keyword arguments
say_hello(language = 'PT', name = 'Jonathan')
say_hello(name = 'Jonathan')
say_hello()



#Local and Global scope
def say_hello(greeting):
    name = input('What`s your name')
    print(greeting, name)

# print(name) #in the global scope "name" is not defined

# global_var = 100

# def calculation(a,b):
#     global global_var
#     addition = a+b
#     substraction = a-b
#     global_var += addition
#     print(f'addition = {addition}\n substraction = {substraction}')
#     print(global_var)

# calculation(5,7)

#returning values
def calculation(a,b):
    addition = a+b
    substraction = a -b

    print(f'addition = {addition}\n')
    return (addition, substraction)

addition, substraction = calculation(8,10)
total_value = 5

def increase_total(addition, total_value, substraction):
    result1 = total_value + addition
    result2 = total_value - substraction
    return (result1, result2)

print(type(increase_total(addition,total_value,substraction)))


