# # excercice 1
# # Print the following output in one line of code:
# print("Hello world\n" * 4)

# # exercise 2
# # Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
# print((99**3)*8)

# # excercice 3
# # Predict the output of the following code snippets:
# print(5 < 3)
# print(3 == 3)
# print(3 == "3")
# try:
#     print("3" > 3)
# except TypeError:
#     print("TypeError: '>' not supported between instances of 'str' and 'int'")
# print("Hello" == "hello")

# # exercise 4
# # Create a variable called computer_brand which value is the brand name of your computer.
# # Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
# computer_brand = 'Asus'
# print(f"I have a {computer_brand} computer")

# # excersice 5
# # Create a variable called name, and set it’s value to your name.
# # Create a variable called age, and set it’s value to your age.
# # Create a variable called shoe_size, and set it’s value to your shoe size.
# # Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# # Have your code print the info message.
# # Run your code
# name = "damian"
# age = 42
# shoe_size = 43
# info = "My name is " + name + ". I'm " + str(age) + " years old and my shoe size is " + str(shoe_size) + "."
# print(info)

# # exercice 6
# # Create two variables, a and b.
# # Each variable value should be a number.
# # If a is bigger then b, have your code print Hello World.
# import random as rd
# a = rd.randint(1, 10)
# b = rd.randint(1, 10)
# print(f"a = {a}\nb = {b}")
# print("hello world") if a > b else None

# # Exercise 7 : Odd or Even
# number = int(input("input your number, floating numbers will be rounded"))
# print("even number") if (number % 2 == 0) else print("odd number")

# # exercise 8
# # Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
# name = input("insert your name")
# output = ["same as me" if name == 'damian' or name == 'Damian' else "a funny message based on the outcome"]
# print(output)

# # Exercise 9
# # Write code that will ask the user for their height in centimeters.
# # If they are over 145cm print a message that states they are tall enough to ride.
# # If they are not tall enough print a message that says they need to grow some more to ride.
# height = int(input("input height in cm"))
# output = ["tall enough to ride" if height >= 145 else "not tall enough to ride"]
# print(output)