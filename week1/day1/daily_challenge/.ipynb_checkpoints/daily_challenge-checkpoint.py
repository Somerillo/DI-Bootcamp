# # Excercise 1
# # Using the input function, ask the user for a string. The string must be 10 characters long.
# # If it’s less than 10 characters, print a message which states “string not long enough”.
# # If it’s more than 10 characters, print a message which states “string too long”.
# # If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
# string = input("insert string")
# if len(string) < 10:
#     print("string not long enough")
# elif len(string) > 10:
#     print("string too long")
# else:
#     print("perfect string")

# # Then, print the first and last characters of the given text
# print(string[0])
# print(string[len(string) - 1])

# # Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed.
# m = ''
# for n in string:
#     m = m + n
#     print(m)

# # Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# import random as rd
# char_list = list(string) # generate a list from the string
# rd.shuffle(char_list) # randomize
# shuffled_text = ''.join(char_list)
# print(shuffled_text)