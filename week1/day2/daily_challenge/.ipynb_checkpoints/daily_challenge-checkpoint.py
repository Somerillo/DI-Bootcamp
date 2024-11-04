# # Challenge 1
# #     Ask the user for a number and a length.
# #     Create a program that prints a list of multiples of the number until the list length reaches length.

# number = int(input("input integer number"))
# length = int(input("input lenght"))

# limit = number * length
# list1 = []

# for num in range(1, length + 1):
#     list1.append(num * number)

# print(list1)



#------------------------------------------------------------------------------------------------------------------------------
# # Challenge 2
# #     Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# string = input("input string")
# list1 = list(string)

# k = ''
# list2=[]
# for char in list1:
#     if char != k:
#         list2.append(char)
#         k = char

# new_string = "".join(list2)
# print(new_string)