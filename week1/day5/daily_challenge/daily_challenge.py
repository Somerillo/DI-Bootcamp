## ------------------------------------------------------------------------------------------------------------------------
# # Challenge 1 : Sorting
# #     Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# #   sequence after sorting them alphabetically.
# #     Use List Comprehension

# # Example:

# # Suppose the following input is supplied to the program: without,hello,bag,world
# # Then, the output should be: bag,hello,without,world

# string = "without,hello,bag,world"

# def func_sorting_1(string):
#     """
#     this one uses list comprehension to strip spaces (if there are) in each word
#     """
#     list_string = [word.strip() for word in string.split(",")]

#     # this for loop does the same as list_string.sort()
#     # i really dont know how to apply list comprehension
#     new_list = []
#     for word in list_string:
#         flag = False
#         for i in range(len(new_list)):
#             if word < new_list[i]: # THIS SORTS ALPHABETICALLY!!!!!!!!
#                 new_list.insert(i, word) # IT IS INSERTED BEFORE THE BIGER WORD!!!!!
#                 flag = True
#                 break
#         # if there`s no word we add it at the end, because the word is "bigger"
#         if not flag:
#             new_list.append(word)

#     string = ",".join(new_list)
#     print(string)

# func_sorting_1(string)

# def func_sorting_2(string):
#     """
#     maybe this is what was asked for
#     """
#     list_string = [word for word in string.split(",")]
#     list_string.sort()
#     string = ",".join(list_string)
#     print(string)

# func_sorting_2(string)



## ------------------------------------------------------------------------------------------------------------------------
# # Challenge 2 : Longest Word
# #     Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# #     Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

# string = "all work and no play makes jack a dull boy"
# string1 = "Margaret's toy is a pretty doll." # ➞ "Margaret's"
# string2 = "A thing of beauty is a joy forever." # ➞ "forever."
# string3 = "Forgetfulness is by all means powerless!" # ➞ "Forgetfulness"

# def longest_word(str):
#     """
#     If two or more words are found, return the first longest word.
#     """
#     list_str = [word for word in str.split(" ")]
#     word = ""
#     for i in range(len(list_str)):
#         if len(word) < len(list_str[i]):
#             word = list_str[i]
#             continue
#     print(word)

# longest_word(string)
# longest_word(string1)
# longest_word(string2)
# longest_word(string3)