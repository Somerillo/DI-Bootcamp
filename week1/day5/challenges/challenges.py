## ------------------------------------------------- Exercise 1 ------------------------------------------------- ##
# # Instructions

# #     Write a script that inserts an item at a defined index in a list.

# list_1 = [2, 4, 23, 325, 98]
# index = 4
# item = "item"
# list_1.insert(index, item)
# print(list_1)


## ------------------------------------------------- Exercise 2 ------------------------------------------------- ##
# # Instructions

# #     Write a script that counts the number of spaces in a string.

# string = "all work and no play makes jack a dull boy"
# k = 0
# for i in range(len(string)):
#     char = string[i]
#     if char == " ":
#         k += 1
# print(f"there are {k} spaces")


## ------------------------------------------------- Exercise 3 ------------------------------------------------- ##
# # Instructions

# #     Write a script that calculates the number of upper case letters and lower case letters in a string.

# string = "All Your Base Are Belong To Us"
# upper = 0
# lower = 0

# for char in string:
#     if char.isupper():
#         upper += 1
#     elif char.islower(): # cant use simply `else` for we dont want to count spaces!!!
#         lower += 1

# print(f"there are {upper} uppercase letters and {lower} lowercase letters in the string")

## ------------------------------------------------- Exercise 4 ------------------------------------------------- ##
# # Instructions

# # Write a function to find the sum of an array without using the built in function:

# #     >>>my_sum([1,5,4,2])
# #     >>>12

# array_1 = [1,5,4,2]

# def my_sum(array = array_1):
#     """
#     finds the sum of an array without using the built in function
#     """
#     num = 0
#     for i in range(len(array)):
#         num = num + array[i]
#     return num

# print(my_sum())

## ------------------------------------------------- Exercise 5 ------------------------------------------------- ##
# # Instructions

# # Write a function to find the max number in a list

# #     >>>find_max([0,1,3,50])
# #     >>>50

# list_1 = [0,1,3,50, -9]

# def find_max(lis = list_1):
#     num = lis[0]
#     for i in range(1, len(lis)):
#         if lis[i] < num:
#             num = lis[i]
#     print(num)

# find_max()    

## ------------------------------------------------- Exercise 6 ------------------------------------------------- ##
# # Instructions

# # Write a function that returns factorial of a number

# #     >>>factorial(4)
# #     >>>24

# number = 4

# def func_fact(num = number):
#     """
#     returns factorial of a number
#     """
#     fact = 1
#     for i in range(1, num + 1):
#         fact = i * fact
#     print(fact)

# func_fact()

## ------------------------------------------------- Exercise 7 ------------------------------------------------- ##
# Instructions

# # Write a function that counts an element in a list (without using the count method):

# #     >>>list_count(['a','a','t','o'],'a')
# #     >>>2

# list_1 = [['a','a','t','o'],'a']

# def list_count(lis = list_1):
#     """
#     counts an element in a list (without using the count method)
#     """
#     print(len(lis))

# list_count()

## ------------------------------------------------- Exercise 8 ------------------------------------------------- ##
# # Instructions

# # Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# #     >>>norm([1,2,2])
# #     >>>3

# list_1 = [1, 2, 2]

# def norm(lis = list_1):
#     """
#     returns the L2-norm
#     """
#     # num = []
#     # for i in range(len(lis)):
#     #     num.append(lis[i] ** 2)
#     num = [lis[i] ** 2 for i in range(len(lis))]
#     num = sum(num) ** 0.5
#     print(num)

# norm()

## ------------------------------------------------- Exercise 9 ------------------------------------------------- ##
# # Instructions

# # Write a function to find if an array is monotonic (sorted either ascending of descending)

# #     >>>is_mono([7,6,5,5,2,0])
# #     >>>True

# #     >>>is_mono([2,3,3,3])
# #     >>>True

# #     >>>is_mono([1,2,0,4])
# #     >>>False

# array_1 = [7,6,5,5,2,0]
# array_2 = [2,3,3,3]
# array_3 = [1,2,0,4]

# def is_mono(arr = array_1):
#     """
#     find if an array is monotonic
#     """
#     asc = 0
#     des = 0
#     lim = len(arr) - 1

#     for i in range(lim):
#         if arr[i] <= arr[i + 1]:
#             asc += 1

#     for i in range(lim):
#         if arr[i] >= arr[i + 1]:
#             des +=1

#     return asc == lim or des == lim

# print(is_mono(array_3))

## ------------------------------------------------- Exercise 10 ------------------------------------------------- ##
# # Instructions

# #     Write a function that prints the longest word in a list.

# string = "a man of focus commitment and sheer will"
# lis_string = string.split()

# def longest_word(lis = lis_string):
#     """
#     prints the longest word in a list
#     """
#     longest = ""
#     for word in lis:
#         if len(longest) < len(word): # returns the first longest, with <= returns the last longest
#             longest = word
#         else:
#             continue
#     print(longest)

# longest_word()

## ------------------------------------------------- Exercise 11 ------------------------------------------------- ##
# # Instructions

# #     Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

# lis_in = ["life universe and everything else", 42, "Farhenheit", 451]
# def partake(lis):
#     """
#     put all the integers in one list, and all the strings in another one
#     """
#     # strings = []
#     # integers = []

#     # for i in lis:
#     #     if isinstance(i, str):
#     #         strings.append(i)
#     #     else:
#     #         integers.append(i)
#     strings = [i for i in lis if isinstance(i, str)]
#     integers = [i for i in lis if isinstance(i, int)]
    
#     print(strings)
#     print(integers)

# partake(lis_in)

## ------------------------------------------------- Exercise 12 ------------------------------------------------- ##
# # Instructions

# # Write a function to check if a string is a palindrome:

# #     >>>is_palindrome('radar')
# #     >>>True

# #     >>>is_palindrome('John)
# #     >>>False

# string_0 = "sator arepo tenet opera rotas"
# string_1 = "radar"
# string_2 = "John"

# def is_palindrome(string):
#     """
#     check if a string is a palindrome
#     """
#     lis = list(string.lower())
#     for i in range(len(lis) // 2):
#         if lis[i] != lis[-(i + 1)]: # la division entera omitio un termino!!!!
#             return False
#         else:
#             return True

# print(is_palindrome(string_0))

## ------------------------------------------------- Exercise 13 ------------------------------------------------- ##
# # Instructions

# # Write a function that returns the amount of words in a sentence with length > k:

# #     >>>sentence = 'Do or do not there is no try'
# #     >>>k=2
# #     >>>sum_over_k(sentence,k)
# #     >>>3

# sentence = 'Do or do not there is no try'
# k = 2

# def sum_over_k(sentence, k):
#     counter = 0
#     for word in sentence.split():
#         if len(word) > k:
#             counter += 1
#     print(counter)

# sum_over_k(sentence, k)

## ------------------------------------------------- Exercise 14 ------------------------------------------------- ##
# # Instructions

# # Write a function that returns the average value in a dictionary (assume the values are numeric):

# #     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# #     >>>3

# dict_1 = {'a': 1,'b':2,'c':8,'d': 1}

# def dict_avg(dic):
#     """
#     returns the average value in a dictionary (assume the values are numeric)
#     """
#     numbers = [i for i in dic.values()]
#     avg = float(sum(numbers)) / float(len(numbers))
#     print(avg)

# dict_avg(dict_1)


## ------------------------------------------------- Exercise 15 ------------------------------------------------- ##
# # Instructions

# # Write a function that returns common divisors of 2 numbers:

# #     >>>common_div(10,20)
# #     >>>[2,5,10]

# def common_div(x = 10, y = 20):
#     """
#     returns common divisors of 2 numbers
#     """
#     divisors_x = [i for i in range(2, x + 1) if x % i == 0]
#     divisors_y = [i for i in range(2, y + 1) if y % i == 0]
#     divisors_common = [num for num in divisors_x if num in divisors_y]
#     print(divisors_common)

# common_div()


## ------------------------------------------------- Exercise 16 ------------------------------------------------- ##
# # Instructions

# # Write a function that test if a number is prime:

# #     >>>is_prime(11)
# #     >>>True

# def is_prime(num = 11):
#     """
#     test if a number is prime
#     """
#     divisors = [i for i in range(2, num) if num % i == 0]
#     print(len(divisors) == 0)

# is_prime(17)


## ------------------------------------------------- Exercise 17 ------------------------------------------------- ##
# # Instructions

# # Write a function that prints elements of a list if the index and the value are even:

# #     >>>weird_print([1,2,2,3,4,5])
# #     >>>[2,4]

# def weird_print(lis):
#     """
#     prints elements of a list if the index and the value are even
#     """
#     num_even = [i for i in lis if i % 2 == 0]
#     output = [lis[i] for i in range(len(lis)) if (lis[i] in num_even) and (i % 2 == 0)]
#     print(output)

# weird_print([1,2,2,3,4,5])

## ------------------------------------------------- Exercise 18 ------------------------------------------------- ##
# # Instructions

# # Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

# #     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
# #     >>>int: 1, str:1 , float:1, bool:2

# def type_count(**kwargs):
#     """
#     accepts an undefined number of keyworded arguments and return the count of different types
#     """
#     type_counts = {}
    
#     for value in kwargs.values():
#         type_name = type(value).__name__
#         if type_name in type_counts:
#             type_counts[type_name] += 1
#         else:
#             type_counts[type_name] = 1
    
#     result = []
#     for type_name, count in type_counts.items():
#         result.append(f"{type_name}: {count}")
    
#     print(result)
#     return ', '.join(result)

# print(type_count(a=1, b='string', c=1.0, d=True, e=False))


## ------------------------------------------------- Exercise 19 ------------------------------------------------- ##
# # Instructions

# #     Write a function that mimics the builtin .split() method for strings.
# #     By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

# def fun_split(string, separator = " "):
#     """
#     mimics the builtin .split()
#     """
    
#     lis = []
#     word = []
#     for char in string:
#         if char == separator:
#             lis.append("".join(word))
#             word = []
#         else:
#             word.append(char)

#     # append the last word if any
#     if word:
#         lis.append("".join(word))

#     print(lis)

# fun_split("all work and no games makes jack a dull boy")

## ------------------------------------------------- Exercise 20 ------------------------------------------------- ##
# # Instructions

# #     Convert a string into password format.

# # Example:
# # input : "mypassword"
# # output: "***********"

# def password_format(string):
#     """
#     Convert a string into password format.
#     """
#     output = "*" * len(string)
#     return output

# print(password_format("mypassword"))