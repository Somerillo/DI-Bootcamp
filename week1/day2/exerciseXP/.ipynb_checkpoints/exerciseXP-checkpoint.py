## # exercise 1
# # Create a set called my_fav_numbers with all your favorites numbers.
# # Add two new numbers to the set.
# # Remove the last number.
# # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# my_fav = {0, -1, 3.14159, 22}
# print(f"my numbers set is {my_fav}")

# my_fav.update([5, 8]) # IMPORTANTE!!! update actualiza el valor de manera directa
# print(f"the new set is {my_fav}")

# my_fav.remove(8) # IMPORTANTE!!! update actualiza el valor de manera directa
# print(f"the new set removing the last added element is {my_fav}")

# friend_fav_numbers = {0., 12, 6.023E23, -1}
# print(f"friend fav nums are {friend_fav_numbers}")

# our_fav_numbers = my_fav.union(friend_fav_numbers)
# print(f"the combined set is {our_fav_numbers}")



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 2
# # Given a tuple which value is integers, is it possible to add more integers to the tuple?
# print("tuples are immutable, therefore we cant add new elements and we have to define a new tuple for that")



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 3: Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# # Remove “Banana” from the list.
# # Remove “Blueberries” from the list.
# # Add “Kiwi” to the end of the list.
# # Add “Apples” to the beginning of the list.
# # Count how many apples are in the basket.
# # Empty the basket.
# # Print(basket)
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# print(basket)

# basket.pop(-1)
# print(basket)

# basket.append("Kiwi")
# print(basket)

# basket.insert(0, "Apples")
# print(basket)

# print(f"there are {basket.count("Apples")} `Apples` in the list")

# basket = []
# print(basket)



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 4: Floats
# # a) Recap – What is a float? What is the difference between an integer and a float?
# print("A float number is a number that includes a decimal point and has more precision. It can be separated in its integer and decimal parts")

# # b) Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# my_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(my_list)

# new_list = range(3, 11, 1)
# new_list = [float(i) / 2. for i in new_list]
# print(new_list) # one way to do it, here all numbers are float

# new_list = [1, 2, 3, 4, 5]
# new_list_2 = [float(i) + .5 for i in new_list]
# new_list.pop(0)
# new_list_2.pop(-1)
# print(sorted(new_list + new_list_2)) # now we have integer and float list combined and sorted :)

# # c) Can you think of another way to generate a sequence of floats?
# import numpy as np
# new_list = np.linspace(1.5, 5.0, 8)
# print(new_list)



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 5: For Loop
# # a) Use a for loop to print all numbers from 1 to 20, inclusive.
# for i in range(1, 21):
#     print(i)

# # b) Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 6: Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
# a = input("insert name as `your name` to stop the loop")
# while a != "your name":
#     a = input("insert name as `your name` to stop the loop")



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 7: Favorite fruits
# # a) Ask the user to input their favorite fruit(s) (one or several fruits).
# # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# fruits = input("insert favorite fruits separated by space as in example: \n`apple mango cherry`\n\n")

# # b) Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# fruits = fruits.split() # we use `.split()` to generate a space separated list

# # c) Now that we have a list of fruits, ask the user to input a name of any fruit.
# #     If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# #     If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# fruit = input("input a name of any fruit")
# if fruit in fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 8: Who ordered a pizza ?
# # a) Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# # b) As they enter each topping, print a message saying you’ll add that topping to their pizza.
# topping = input("input topping, after finishing list input `quit` to exit")
# toppings = []
# while topping != "quit":
#     toppings.append(topping)
#     print("you’ll add that topping to their pizza\n")
#     topping = input("input new topping, or `quit` to exit")

# # c) Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
# print(f"Your toppings list is: {toppings}")
# print(f"The total price is: {10. + float(len(toppings)) * 2.5:.2f}")



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 9: Cinemax
# # a) A movie theater charges different ticket prices depending on a person’s age.
# #     if a person is under the age of 3, the ticket is free.
# #     if they are between 3 and 12, the ticket is $10.
# #     if they are over the age of 12, the ticket is $15.

# # b) Ask a family the age of each person who wants a ticket.

# # c) Store the total cost of all the family’s tickets and print it out.

# price = 0
# while True:
#     age = input("input age to buy ticket, or input `q` to quit")

#     if age == "q": # we check if the user wants to exit
#         break

#     age = int(age) # transform string to number

#     if age <= 3:
#         continue
#     elif 3 < age <= 12:
#         price += 10
#     elif 12 < age:
#         price += 15

# print(f"tot. price: {price}")


# # d) A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# # Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# # At the end, print the final list.

# names = ["Name1", "Name2", "Name3", "Name4"] # list of banned teenagers
# for name in names:
#     age = int(input(f"hello {name}, input your age"))

#     if 16 <= age < 21:
#         print(f"age restriction, {name} not allowed")
#         names.remove(name)

# print(f"allowed teenagers list is: {names}")



# -----------------------------------------------------------------------------------------------------------------------
# # Exercise 10 : Sandwich Orders
# # Using the list below :
# # sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# # a)    The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")
# print(sandwich_orders)

# # b)    We need to prepare the orders of the clients:
# #         Create an empty list called finished_sandwiches.
# #         One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# # c)    After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# # I made your tuna sandwich
# # I made your avocado sandwich
# # I made your egg sandwich
# # I made your chicken sandwich
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop(0)
#     print(f"i made your {sandwich}")
#     finished_sandwiches.append(sandwich)
# print("pending sandwich list: ", sandwich_orders)
# print("finished sandwich list: ", finished_sandwiches)