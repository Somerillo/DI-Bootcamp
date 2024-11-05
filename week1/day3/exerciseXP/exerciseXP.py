# # Exercise 1 : Convert lists into dictionaries
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# expected_output = dict(zip(keys, values))
# print(expected_output)




### ----------------------------------------------------------------------------------------------------------------------
# Exercise 2 : Cinemax #2
# Instructions

#     A movie theater charges different ticket prices depending on a person’s age.
#         if a person is under the age of 3, the ticket is free.
#         if they are between 3 and 12, the ticket is $10.
#         if they are over the age of 12, the ticket is $15.

#     Given the following object:

#     family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


#     How much does each family member have to pay ?
#     Print out the family’s total cost for the movies.
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# def entrance_cost(age):
#     if age < 3:
#         return 0
#     elif 3 <= age < 12:
#         return 10
#     elif age >= 12:
#         return 15

# tot_price = 0
# for name in family.keys():
#     age = family[name]
#     price = entrance_cost(age)
#     tot_price += price
#     print(f"{name} has to pay ${price}")

# print(f"Tot. price is ${tot_price}")

### Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
# family = {}
# stop = int(input("Input how many family members are"))
# tot_price = 0

# def entrance_cost(age):
#     if age < 3:
#         return 0
#     elif 3 <= age < 12:
#         return 10
#     elif age >= 12:
#         return 15

# for i in range(stop):
#     name = input("input name (repeated names are not allowed)")
#     age = int(input("input age"))
#     family[name] = age

# tot_price = 0
# for name in family.keys():
#     age = family[name]
#     price = entrance_cost(age)
#     tot_price += price
#     print(f"{name} has to pay ${price}")

# print(f"Tot. price is ${tot_price}")




### ----------------------------------------------------------------------------------------------------------------------
# # Exercise 3: Zara
# # Instructions

# #     Here is some information about a brand.

# #     name: Zara 
# #     creation_date: 1975 
# #     creator_name: Amancio Ortega Gaona 
# #     type_of_clothes: men, women, children, home 
# #     international_competitors: Gap, H&M, Benetton 
# #     number_stores: 7000 
# #     major_color: 
# #         France: blue, 
# #         Spain: red, 
# #         US: pink, green



# #     2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# #     The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": [
#         "men",
#         "women", 
#         "children", 
#         "home"
#     ],
#     "international_competitors": [
#         "Gap", 
#         "H&M", 
#         "Benetton"
#     ],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue", 
#         "Spain": "red", 
#         "US": ["pink", 
#                "green"
#         ]
#     }
# }



# #     3. Change the number of stores to 2.
# brand["number_stores"] = 2
# print(f"3. number_stores = {brand["number_stores"]}")
# print()



# #     4. Print a sentence that explains who Zaras clients are.
# print(f"4. Zara`s clients are {brand["type_of_clothes"]}")
# print()



# #     5. Add a key called country_creation with a value of Spain.
# brand["country_creation"] = "Spain"
# print("5. ", brand["country_creation"])
# print()



# #     6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# if "international_competitors" in brand.keys():
#     print("The key `international_competitors` is in the dictionary")
#     brand["international_competitors"].append("Desigual")
#     print("6. ", brand["international_competitors"])

# print()


# #     7. Delete the information about the date of creation.
# del brand["creation_date"]
# print("7. ", brand.keys())
# print()



# #     8. Print the last international competitor.
# print(f"8. last intl competitor is{brand["international_competitors"][-1]}")
# print()



# #     9. Print the major clothes colors in the US.
# print(f"9. major clothes colors in the US {brand["major_color"]["US"]}")
# print()



# #     10. Print the amount of key value pairs (ie. length of the dictionary).
# print(f"10. length of the dictionary is {len(brand.keys())}")
# print()



# #     11. Print the keys of the dictionary.
# print(f"11. dict keys are: {brand.keys()}")
# print()



# #     12. Create another dictionary called more_on_zara with the following details:
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }
# print(f"12. the new dict more_on_zara is: {more_on_zara}")
# print()



# #     13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# brand.update(more_on_zara)
# print(f"13. the updated `brand` dictionary is: {brand}")
# print()



# #     14. Print the value of the key number_stores. What just happened ?
# print(f"14. the updated number_stores is: {brand["number_stores"]}")
# print("The original value was overwritten by the `more_on_zara` update")



## ---------------------------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------------------
# # Exercise 4 : Disney characters
# # 1.    Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# # >>> print(disney_users_A)
# # {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {}
# k = 0 # instantiate the counter

# for key in users:
#     disney_users_A[key] = k
#     k += 1

# print(disney_users_A)




# # 2.    Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# # >>> print(disney_users_B)
# # {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_B = {}
# k = 1 # instantiate the counter

# for key in users:
#     disney_users_B[key] = k
#     k += 1

# print(disney_users_B)



# # 3.    Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# # >>> print(disney_users_C)
# # {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# users.sort()
# print(users)

# disney_users_C = {}
# k = 0 # instantiate the counter

# for key in users:
#     disney_users_C[key] = k
#     k += 1

# print(disney_users_C)



# # 4.    Only recreate the 1st result for:
# #         The characters, which names contain the letter “i”.
# #         The characters, which names start with the letter “m” or “p”.
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# disney_users_A = {}
# k = 0 # instantiate the counter

# for key in users:
#     disney_users_A[key] = k
#     k += 1

# print(disney_users_A)

# keys_A = []
# keys_B = []
# users_A = {}
# users_B = {}

# for user in users:
#     if "i" in list(user):
#         keys_A.append(user)
#         users_A[user] = disney_users_A[user]
#     if ("m" == list(user)[0].lower()) or ("p" == list(user)[0].lower()):
#         keys_B.append(user)
#         users_B[user] = disney_users_A[user]

# values = list(range(0, 10))
# dict1 = dict(zip(keys_A, values))
# dict2 = dict(zip(keys_B, values))

# print("\nI didn`t understand if the consign was this:")
# print(dict1)
# print(dict2)
# print()
# print("or this:")
# print(users_A)
# print(users_B)