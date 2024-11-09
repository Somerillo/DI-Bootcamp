#     Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#     Display a little cake as seen below:

#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

import datetime

cake = [
    "       ___________",
    "      |:H:a:p:p:y:|",
    "    __|___________|__",
    "   |^^^^^^^^^^^^^^^^^|",
    "   |:B:i:r:t:h:d:a:y:|",
    "   |                 |",
    "   ~~~~~~~~~~~~~~~~~~~"
]


year_now = datetime.datetime.now().year
year_birth = int(input("input year of birth: "))
# age = year_now - year_birth
last_digit = (year_now - year_birth) % 10

top = "       __" + "_" * int(4 - last_digit / 2) + \
    last_digit * "i" + "_" * int(4 - last_digit / 2) + "__"

if last_digit % 2 == 0:
    top = top[:13] + "_" + top[13:]
    top = top[:6] + " " + top[8:]
    top = top[:-1]
cake[0] = top

if year_birth % 4 == 0:
    for i in range(len(cake)):
        print(cake[i])

for i in range(len(cake)):
    print(cake[i])
