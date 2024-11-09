## -------------------------------------------------- Exercise 1: Concatenate lists -------------------------------------------------- ##
# # Write code that concatenates two lists together without using the + sign.

# string1 = "lksegnvolersnld"
# string2 = "oehnverkmvlekrml;ewc"

# string_final = string1 + string2
# print(string_final)


## -------------------------------------------------- Exercise 2: Range of numbers -------------------------------------------------- ##
# # Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# for i in range(1500, 2501):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)


## -------------------------------------------------- Exercise 3: Check the index -------------------------------------------------- ##
# # Using this variable

# # names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# #     Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

# #     Example: if input is 'Cortana' we should be printing the index 1

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# name = input("input name: ")

# if name in names:
#     print(names.index(name))


## -------------------------------------------------- Exercise 4: Greatest Number -------------------------------------------------- ##
# # Ask the user for 3 numbers and print the greatest number.

# #     Test Data
# #     Input the 1st number: 25
# #     Input the 2nd number: 78
# #     Input the 3rd number: 87

# #     The greatest number is: 87

# num1 = float(input("input 1st number: "))
# num2 = float(input("input 2nd number: "))
# num3 = float(input("input 3rd number: "))
# print(max(num1, num2, num3))


## -------------------------------------------------- Exercise 5: The Alphabet -------------------------------------------------- ##
# # Instructions

# #     Create a string of all the letters in the alphabet
# #     Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

# string = [chr(i) for i in range(97, 123)]
# vowels = ["a", "e", "i", "o", "u"]

# for char in string:
#     if char in vowels:
#         print(f"{char} is a vocal")
#     else:
#         print(f"{char} is a consonant")


## -------------------------------------------------- Exercise 6: Words and letters -------------------------------------------------- ##
# #     Ask a user for 7 words, store them in a list named words.
# #     Ask the user for a single character, store it in a variable called letter.
# #     Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# #     If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

# words = [input(f"input word {i+1}: ") for i in range(7)]
# letter = input("input character: ")
# for word in words:
#     if letter in word:
#         print(f"first appearance of {letter} in {
#               word} is in index {word.index(letter)}")
#     else:
#         print(f"a friendly message with {word} and {letter}")


## -------------------------------------------------- Exercise 7: Min, Max, Sum -------------------------------------------------- ##
# # Instructions

# #     Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts
# #  at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

# lis = [i for i in range(1, int(1e6) + 1)]
# print(f"minimum = {min(lis)}; maximum = {max(lis)}")
# print(sum(lis))


## -------------------------------------------------- Exercise 8 : List and Tuple -------------------------------------------------- ##
# # Instructions

# #     Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

# # Suppose the following input is supplied to the program: 34,67,55,33,12,98

# # Then, the output should be:

# # ['34', '67', '55', '33', '12', '98']
# # ('34', '67', '55', '33', '12', '98')

# # string = input("input sequence")
# string = "34,67,55,33,12,98"
# lis = string.split(",")
# tup = tuple(lis)
# print(f"{lis}\n{tup}")


## -------------------------------------------------- Exercise 9 : Random number -------------------------------------------------- ##
# # Instructions

# #     Ask the user to input a number from 1 to 9 (including).
# #     Get a random number between 1 and 9. Hint: random module.
# #     If the user guesses the correct number print a message that says Winner.
# #     If the user guesses the wrong number print a message that says better luck next time.
# #     Bonus: use a loop that allows the user to keep guessing until they want to quit.
# #     Bonus 2: on exiting the loop tally up and display total games won and lost.

# import random

# games_won = 0
# games_lost = 0

# while True:
#     num_rand = random.randint(1, 9)
#     num_user = input("input number from 1 to 9, or 'q' to exit: ")

#     if num_user.lower() == 'q':
#         break

#     try:
#         num_user = int(num_user)
#         if not 1 <= num_user <= 9:
#             raise ValueError
#     except ValueError:
#         print("invalid entry, input from 1 to 9")
#         continue

#     if num_rand == num_user:
#         print("Winner")
#         games_won += 1
#     else:
#         print(f"better luck next time, the number was {num_rand}.")
#         games_lost += 1

# print(f"\nwon games: {games_won}")
# print(f"lost games: {games_lost}")
# print(f"total games: {games_won + games_lost}")
