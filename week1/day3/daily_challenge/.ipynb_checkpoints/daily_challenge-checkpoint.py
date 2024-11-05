# # -----------------------------------------------------------------------------------------------------------------
# # Challenge 1

# #     Ask a user for a word

# #     Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# #         Make sure the letters are the keys.
# #         Make sure the letters are strings.
# #         Make sure the indexes are stored in a list and those lists are values.
# word = input("word")
# list_word = list(word)
# dict_char = {}
# k=0

# for char in list_word:
#     if char not in dict_char:
#         dict_char[char] = [] # need initiate an empty list before adding!!!!!!!!!!
#     dict_char[char].append(k)
#     k += 1

# print(dict_char)




# # -----------------------------------------------------------------------------------------------------------------
# Challenge 2

#     Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
#     Sort the list in alphabetical order.
#     Return “Nothing” if you can’t afford anything from the store.

print("Before running: uncomment desired `items_purchase` list and `wallet` ammount.")
print()

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

## ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

## ➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# # In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan, 
# # instead you can by the Spoon that is $2

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

## ➞ "Nothing"


# # we convert to int the wallet value
# list_wallet = list(wallet)
# if "," in list_wallet:
#     list_wallet.remove(",")
# if "$" in list_wallet:
#     list_wallet.remove("$")

# wallet = int("".join(list_wallet))

# # we compare prices to the wallet swepping items in the loop
# list_items = []
# total_cost = 0
# for key in items_purchase.keys():
#     item = key
#     item_cost = items_purchase[key]

#     # we convert to int the item cost
#     list_item_cost = list(item_cost)
#     if "," in list_item_cost:
#         list_item_cost.remove(",")
#     if "$" in list_item_cost:
#         list_item_cost.remove("$")

#     item_cost = int("".join(list_item_cost))


#     if (total_cost + item_cost) < wallet:
#         total_cost += item_cost
#         list_items.append(key)
#         list_items.sort()

# if total_cost == 0:
#     print("Nothing")
# else:
#     print(list_items)