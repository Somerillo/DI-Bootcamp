greetings = 'Shabat shalom'

print(greetings[3])

#slicing
print(greetings[2:-1])

# string most used methods
print(len(greetings))

print('index of space:', greetings.index(' '))

print('hello'.capitalize())
print('hello'.upper())
print('hello world'.title())
print(greetings.replace('shalom', 'mebura'))
print(greetings)

student = 'Harry Potter  '
student = student.strip()
print(student + greetings)

texto = "abcHola, mundo!cba"
texto_limpio = texto.strip("abc")
print(texto_limpio)  # "Hola, mundo!"


#numbers: integ, float, complex, bool

my_num = 5 #int: whole numb
float_num = 5.

#operations
print(my_num + float_num)

print((greetings + " ") *3)
print(round(5/3,3))
print(11//3) # floor division
print(11%3)

if 12%3 == 0:
    print('yes')

my_age = 123879 + 42
#print(my_age)
print('extremely old')

age = input('insert age')
print(int(age) + 1)

# comparison operators
print(5!=2)

print(5==5)

f_name = 'max'
l_name = 'power'

print(f'hello {f_name} {l_name}')

print('something' is 'something')