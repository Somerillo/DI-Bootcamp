## --------------------------------------------------- Exercise 1 --------------------------------------------------- ##
# #     Draw the following pattern using for loops:

# #   *
# #  ***
# # *****

# def print_pine(rows = 3):
#     """
#     prints a pine tree inefficiently, then efficiently
#     """
#     for i in range(1, rows + 1): # rows
#         right = i * "*"
#         right_cutted = (i - 1) * "*"
#         left_spaces = (rows - i) * " "
#         left = left_spaces + right
#         print(left + right_cutted) # this is not the most efficient way... lets do it better

#     print()

#     for i in range(rows): # this is the right way
#         spaces = " " * (rows - i - 1) # left spaces
#         asteriscs = "*" * (2 * i + 1) # number of asteriscs
#         print(spaces + asteriscs)

# print_pine()

## ---------------------------------------------------

# #     Draw the following pattern using for loops:

# #     *
# #    **
# #   ***
# #  ****
# # *****

# rows = 5
# for i in range(rows):
#     spaces = " " * (rows - i - 1)
#     asteriscs = "*" * (i + 1)
#     print(spaces + asteriscs)

## ---------------------------------------------------

# #     Draw the following pattern using for loops:

# # *
# # **
# # ***
# # ****
# # *****
# # *****
# #  ****
# #   ***
# #    **
# #     *

# rows = 5

# for i in range(rows):
#     upper = (i + 1) * "*"
#     print(upper)

# for i in range(rows):
#     lower = (i * " ") + ("*" * (rows - i))
#     print(lower)


## --------------------------------------------------- Exercise 2 --------------------------------------------------- ##
# Analyse this code before executing it. Write some commnts next to each line.
# Write the value of each variable and their changes, and add the final output.
# Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233, 24]
for i in range(len(my_list) - 1): # it starts in 0 and performs one iteration less than the whole list length
    minimum = i # starts in 0
    for j in range( i + 1, len(my_list)): # it starts in 1  and performs one iteration less than the whole list length
        if(my_list[j] < my_list[minimum]): # it checks the value of the j-th number in the list vs the i-th one
            minimum = j # if the j-th is lower, we take that value
            if(minimum != i): # it checks the new minimum doesnt take the iteration value from the 1st for loop I DONT KNOW WHY
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # if the first value is bigger than the second, then they are inverted
print(my_list)

# this code sorts ascending the list, rearranges it by checking the elements in couples