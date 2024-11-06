# ## ----------------------------------------------------------------------------------------------------------------
# # Exercise 1 : What are you learning ?
# #     Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# #     Call the function, and make sure the message displays correctly.

# def display_message():
#     """
#     prints one sentence telling everyone what you are learning in this course
#     """
#     print("python coding: lists, dictionaries, sets, tupples, etc")

# display_message()



## ----------------------------------------------------------------------------------------------------------------
# # Exercise 2: What’s your favorite book ?
# #     Write a function called favorite_book() that accepts one parameter called title.
# #     The function should print a message, such as "One of my favorite books is <title>".
# #     For example: “One of my favorite books is Alice in Wonderland”
# #     Call the function, make sure to include a book title as an argument when calling the function.
# def favorite_book(title):
#     """
#     print a message, such as "One of my favorite books is <title>"
#     """
#     print(f"One of my favorite books is `{title}`.")

# title = "A Clockwork Orange"
# favorite_book(title)



## ----------------------------------------------------------------------------------------------------------------
# # Exercise 3 : Some Geography
# #     Write a function called describe_city() that accepts the name of a city and its country as parameters.
# #     The function should print a simple sentence, such as "<city> is in <country>".
# #     For example “Reykjavik is in Iceland”
# #     Give the country parameter a default value.
# #     Call your function.
# def describe_city(city, country = "USA"):
#     """
#     print a simple sentence, such as "<city> is in <country>"
#     """
#     print(f"{city} is in {country}.")

# describe_city("Kentuky")
# describe_city("Quito", "Ecuador")



## ----------------------------------------------------------------------------------------------------------------
# # Exercise 4 : Random
# #     Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# #     Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# import random as rnd

# def rand_function(number):
#     """
#     accepts a number between 1 and 100 and generates another number randomly between 1 and 100
#     if it’s the same number, display a success message, otherwise show a fail message and display both numbers
#     """
#     rnd_number = rnd.randint(1, 100) # the range includes both limits!!!
#     int_number = round(number)
    
#     if rnd_number == int_number:
#         print("a success message")
#     else:
#         print("a fail message")
#         print(f"Input number was {int_number}, random number was {rnd_number}.")

# num = 26.5
# rand_function(num)



## ----------------------------------------------------------------------------------------------------------------
# # Exercise 5 : Let’s create some personalized shirts !
# #     Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# #     The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# #     Call the function make_shirt().

# #     Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# #     Call the function, in order to make a large shirt with the default message
# #     Make medium shirt with the default message
# #     Make a shirt of any size with a different message.

# #     Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(tshirt_size = "Large", message = "I love Python"):
#     """
#     print a sentence summarizing the size of the shirt and the message printed on it
#     """
#     print(f"The size of the shirt is < {tshirt_size} > and the text is < {message} >.")

# make_shirt("XLarge", "42")
# make_shirt()
# make_shirt(tshirt_size="Medium", message="Python is awesome!")
# make_shirt(message="Coding is fun", tshirt_size="Small")
# make_shirt(tshirt_size="XXLarge")
# make_shirt(message="Hello, World!")



## ----------------------------------------------------------------------------------------------------------------
# # Exercise 6 : Magicians …
# # Using this list of magician’s names

# # magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# #     Create a function called show_magicians(), which prints the name of each magician in the list.
# #     Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# #     Call the function make_great().
# #     Call the function show_magicians() to see that the list has actually been modified.

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(list1 = magician_names):
#     """
#     prints the name of each magician in the list
#     """
#     [print(x) for x in list1]
#     print()

# show_magicians()



# def make_great(list1 = magician_names):
#     """
#     adding the phrase "the Great" to each magician’s name
#     """
#     # `[:]` is called "slice notation", and modifies the list in-place!!!!!!!!
#     list1[:] = [x + " the Great" for x in list1]
#     return list1


# make_great()
# print(magician_names)
# print()
# show_magicians()



## ----------------------------------------------------------------------------------------------------------------
# Exercise 7 : Temperature Advice
#     Create a function called get_random_temp().
#         This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#         Test your function to make sure it generates expected results.

#     Create a function called main().
#         Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#         Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

#     Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#         below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#         between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#         between 16 and 23
#         between 24 and 32
#         between 32 and 40

#     Change the get_random_temp() function:
#         Add a parameter to the function, named ‘season’.
#         Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper
#        limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#         Now that we’ve changed get_random_temp(), let’s change the main() function:
#             Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly.
#             Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#             Use the season as an argument when calling get_random_temp().

# import random as rnd
# def get_random_temp(season = "winter"):
#     """
#     return an integer between -10 and 40 degrees
#     """
#     if season == "winter":
#         lower = -10
#         upper = 5

#     elif season in ["spring", "autumn"]:
#         lower = 5
#         upper = 30

#     elif season == "summer":
#         lower = 25
#         upper = 40
        
#     temp = rnd.randint(lower, upper)
#     return temp

# get_random_temp("summer")


# user_season = input(f"Input if season is: summer, sring, winter or autumn")
# def main(season):
#     """
#     Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#     Inform the user of the temperature in a friendly message
#     """
#     temp = get_random_temp(season)
    
#     if temp < 0:
#         string = f"The temperature right now is {temp} degrees Celsius.\nBrrr, that’s freezing! Wear some extra layers today"

#     elif 0 <= temp < 16:
#         string = f"The temperature right now is {temp} degrees Celsius.\nQuite chilly! Don’t forget your coat"

#     elif 16 <= temp < 23:
#         string = f"The temperature right now is {temp} degrees Celsius.\n< Message 3 >"

#     elif 23 <= temp < 32:
#         string = f"The temperature right now is {temp} degrees Celsius.\n< Message 4 >"

#     elif 32 <= temp < 40:
#         string = f"The temperature right now is {temp} degrees Celsius.\n< Message 5 >"
        
#     print(string)

# main(user_season)



# #     Bonus: Give the temperature as a floating-point number instead of an integer.
# #     Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
# def func_season():
#     """
#     season based on month, north hemisf
#     integer month number
#     """
#     month = int(input(f"input month as integer number"))
    
#     if month in [12, 1, 2]:
#         return "winter"
#     elif month in [3, 4, 5]:
#         return "spring"
#     elif month in [6, 7, 8]:
#         return "summer"
#     else:
#         return "autumn"


# def get_random_temp(season):
#     """
#     return an integer between -10 and 40 degrees
#     """
#     if season == "winter":
#         lower = -10
#         upper = 5

#     elif season in ["spring", "autumn"]:
#         lower = 5
#         upper = 30

#     elif season == "summer":
#         lower = 25
#         upper = 40
        
#     temp = round(rnd.uniform(lower, upper), 1)
#     return temp



# def main():
#     """
#     Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#     Inform the user of the temperature in a friendly message
#     """
#     season = func_season()
#     temp = get_random_temp(season)
    
#     if temp < 0:
#         string = f"The temperature right now is {temp} degrees Celsius.\nBrrr, that’s freezing! Wear some extra layers today"

#     elif 0 <= temp < 16:
#         string = f"The temperature right now is {temp} degrees Celsius.\nQuite chilly! Don’t forget your coat"

#     elif 16 <= temp < 23:
#         string = f"The temperature right now is {temp} degrees Celsius.\n< Message 3 >"

#     elif 23 <= temp < 32:
#         string = f"The temperature right now is {temp} degrees Celsius.\n< Message 4 >"

#     elif 32 <= temp < 40:
#         string = f"The temperature right now is {temp} degrees Celsius.\n< Message 5 >"
        
#     print(string)



# main()




## ----------------------------------------------------------------------------------------------------------------
# # Exercise 8 : Star Wars Quiz
# # This project allows users to take a quiz to test their Star Wars knowledge.
# # The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# # 1.    Create a function that asks the questions to the user, and check his answers.
# #     Track the number of correct, incorrect answers. Create a list of wrong_answers
# # 2.    Create a function that informs the user of his number of correct/incorrect answers.
# # 3.    Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# # 4.    If he had more then 3 wrong answers, ask him to play again.
# import random
# from random import shuffle

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# def fun_trivia():
#     # nth = random.randint(0, len(data) - 1) # the upper limit is included and is len - 1
#     random.shuffle(data) # we shuffle the list to alter questions order
#     list_wrong = []
#     k_right = 0
#     k_wrong = 0
#     k_question = 0

#     for index in data:
#         k_question += 1
#         user_answer = input(f"Question {k_question} of 6: {index["question"]}") # take user answer
#         print()
#         right_answer = index["answer"]
        
#         if user_answer.lower() == right_answer.lower():
#             k_right += 1
#             print(f"Correct. You have {k_right} right answers and {k_wrong} wrong answers.\n--------------------------------------\n")
    
#         if user_answer.lower() != right_answer.lower():
#             k_wrong += 1
#             list_wrong.append(user_answer)
#             print(f"WRONG!!!!. You have {k_right} right answers and {k_wrong} wrong answers.")
#             print(f"The right answer is `{right_answer}`; but you answered `{user_answer}`")
#             print("--------------------------------------\n")

#     if k_wrong >= 3:
#         print("play again")
    
#     return list_wrong

# # fun_trivia()
# print(f"Your wrong answers were: {fun_trivia()}")