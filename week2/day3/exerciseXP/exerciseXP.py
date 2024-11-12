################################################
#  _   _           _          ___   ___  ____  #
# (_) | |__   __ _| |_ ___   / _ \ / _ \|  _ \ #
# | | | '_ \ / _` | __/ _ \ | | | | | | | |_) |#
# | | | | | | (_| | ||  __/ | |_| | |_| |  __/ #
# |_| |_| |_|\__,_|\__\___|  \___/ \___/|_|    #
################################################

## ----------------------------------------- Exercise 1: Currencies ----------------------------------------- ##
# # Instructions

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     # Your code starts HERE

#     def __str__(self):
#         """returns a string of the currency"""
#         return f"{self.amount} {self.currency}{'s' if self.amount != 1 else ''}"

#     def __int__(self):
#         """returns `amount` as an integer"""
#         return int(self.amount)

#     def __repr__(self):
#         """returns a string of the currency (just as __str__)."""
#         return self.__str__()

#     def __add__(self, other):
#         """it implements addition"""
#         if isinstance(other, (int, float)):  # verify its an int or a float instance!!!!!!!!!!!
#             return Currency(self.currency, self.amount + other)
#         elif isinstance(other, Currency):  # verify its the same currency
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             raise TypeError("unsupported input type for the sum")

#     def __iadd__(self, other):
#         """it implements addition in-place (+=)."""
#         if isinstance(other, (int, float)):
#             self.amount += other
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             self.amount += other.amount
#         else:
#             raise TypeError("unsupported input type for the sum")
#         return self


# #     Using the code above, implement the relevant methods and dunder methods which will output the results below.
# #     Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))
# # '5 dollars'

# print(int(c1))
# # 5

# print(repr(c1))
# # '5 dollars'

# print(c1 + 5)
# # 10

# print(c1 + c2)
# # 15

# print(c1)
# # 5 dollars

# c1 += 5
# print(c1)
# # 10 dollars

# c1 += c2
# print(c1)
# # 20 dollars

# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>


## ----------------------------------------- Exercise 2: Import ----------------------------------------- ##
# 1-    In a file named func.py create a function that sum 2 numbers, and prints the result
# 2-   In a file named exercise_one.py import the function and call it to print the result

# # Hint: You can use the the following syntaxes:

# import module_name

# OR

# from module_name import function_name

# OR

# from module_name import function_name as fn

# OR

# import module_name as mn


## ----------------------------------------- Exercise 3: String module ----------------------------------------- ##
# #     Generate random String of length 5
# #     Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# #     Hint: use the string module

# import random
# import string

# rand_string_1 = []
# for i in range(5):
#     coin = random.randint(1, 2)
#     if coin % 2 == 0:
#         rand_string_1.append(chr(random.randint(97, 122)))
#     else:
#         rand_string_1.append(chr(random.randint(65, 90)))
# print("".join(rand_string_1))

# rand_string_2 = "".join(random.choices(string.ascii_letters, k=5))
# print(rand_string_2)

## ----------------------------------------- Exercise 4 : Current Date ----------------------------------------- ##
# #     Create a function that displays the current date.
# #     Hint : Use the datetime module.

# import datetime

# def func_time():
#     print(datetime.datetime.now().date())

# func_time()

## ----------------------------------------- Exercise 5 : Amount of time left until January 1st ----------------------------------------- ##
# #     Create a function that displays the amount of time left from now until January 1st.
# #     (Example: the 1st of January is in 10 days and 10:34:01hours).

# import datetime


# def remaining_time(year, month, day):
#     print(f"the {day} of {month} of {year} is in {datetime.datetime(year, month, day) - datetime.datetime.now()} hours")


# remaining_time(2025, 1, 1)

## ----------------------------------------- Exercise 6 : Birthday and minutes ----------------------------------------- ##
# #      Create a function that accepts a birthdate as an argument (in the format of your choice),
# #  then displays a message stating how many minutes the user lived in his life.

# import datetime


# def total_lived_time(birth_year, birth_month, birth_day):
#     total_lived_time = datetime.datetime.now() - datetime.datetime(birth_year,
#                                                                    birth_month, birth_day)
#     print(total_lived_time.total_seconds() / 60)


# total_lived_time(2004, 1, 1)

## ----------------------------------------- Exercise 7 : Faker Module ----------------------------------------- ##
# #     Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# #     Create an empty list called users. Tip: It should be a list of dictionaries.
# #     Create a function that adds new dictionaries to the users list. Each user has the following keys: name,
# #  adress, langage_code. Use faker to populate them with fake data.

# from faker import Faker
# fake = Faker()

# users = []


# def a_function():
#     """
#     adds new dictionaries to the users list
#     """
#     user = {
#         "name": fake.name(),
#         "address": fake.address(),
#         "language_code": fake.language_code()
#     }
#     users.append(user)

# for i in range(10):
#     a_function()

# for user in users:
#     print(user)