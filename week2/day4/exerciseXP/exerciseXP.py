# # ------------------------------------- Exercise 1 – Random Sentence Generator ------------------------------------- # #
# # Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# # Hint : The generated sentences do not have to make sense.

# #     Download this word list

# #     Save it in your development directory.

# #     Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection.
# #  What is the correct data type to store the words?

# #     Create another function called get_random_sentence which takes a single parameter called length.
# #  The length parameter will be used to determine how many words the sentence should have. The function should:
# #         use the words list to get your random words.
# #         the amount of words should be the value of the length parameter.
# #     Take the random words and create a sentence (using a python method), the sentence should be lower case.

# #     Create a function called main which will:
# #         Print a message explaining what the program does.

# #         Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
# # Validate your data and test your validation!
# #             If the user inputs incorrect data, print an error message and end the program.
# #             If the user inputs correct data, run your code.

# import random


# def get_words_from_file(filename):
#     """
#     reads the file`s content and return the words as a collection
#     """
#     words = []
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             # words.append(line)
#             words.append(line.rstrip("\n"))
#     return words


# filename = "sowpods.txt"
# all_the_words = get_words_from_file(filename)
# # print(all_the_words[5:8])


# def get_random_sentence(word_list, length=1):
#     """
#     takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have
#     """
#     sentence = ""
#     for i in range(length):
#         word = (random.choice(word_list)).lower()
#         sentence = sentence + " " + word
#     return sentence
# # print(get_random_sentence(all_the_words, 5))


# def main():
#     """
#     Asks the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
#     """
#     while True:
#         try:
#             length = int(input(
#                 "how long they want the sentence to be. Acceptable values are: an integer between 2 and 20: "))
#             if 2 <= length <= 20:
#                 break
#             else:
#                 print("number must be between 2 and 20")
#         except ValueError:
#             print("insert a valid value")

#     filename = "sowpods.txt"
#     all_the_words = get_words_from_file(filename)

#     print(get_random_sentence(all_the_words, length))


# main()


# # ------------------------------------- Exercise 2: Working with JSON ------------------------------------- # #

# #  Exercise 2: Working with JSON
# # Instructions

# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# #   Access the nested “salary” key from the JSON-string above.
# data = json.loads(sampleJson)  # convert the json string to python ditionary
# print(data)

# salary = data["company"]["employee"]["payable"]["salary"]
# print(salary)


# #   Add a key called “birth_date” to the JSON-string at the same level as the “name” key
# data["company"]["employee"]["birth_date"] = ""


# #   Save the dictionary as JSON to a file.
# with open("employee_data.json", "w") as json_file: # it will overwrite the file
#     json.dump(data, json_file, indent=4)  # indentation 4
