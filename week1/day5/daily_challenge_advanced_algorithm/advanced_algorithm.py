## -------------------------------------------   Daily challenge : Advanced Algorithm   ------------------------------------------- ##

# Last Updated: September 13th, 2024

# What You will learn :

#     Python Basics
#     Conditionals
#     Loops
#     Functions


# Instructions

# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728


# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

# For example

# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728

k = 0
output = []
while list_of_numbers:
    print(len(list_of_numbers)) # regresive count

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[0] + list_of_numbers[i] == target_number:
            output.append((list_of_numbers[0], list_of_numbers[i]))
    list_of_numbers.pop(0)

print(output)
print(f"There are {len(output)} tuples of numbers that sum {target_number}")