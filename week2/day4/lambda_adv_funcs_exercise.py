people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

#discover if the len(name) <= 4
#say hello just for those that len(name) <= 4
# use map() and filter()

filtered_names = list(filter(lambda name: len(name) <= 4, people))
print(filtered_names)

say_hello = list(map(lambda name: f'Hello {name}', filtered_names))
print(say_hello)

