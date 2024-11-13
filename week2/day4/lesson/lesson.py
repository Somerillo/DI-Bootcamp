# # old school style
# try:
#     f = open('sample.txt', 'r=')
#     content = f.read()
#     print(ConnectionResetError)
# finally:
#     f.close()

# with open('sample.txt', "w+", encoding="utf-8") as f:
#     for i in range(1,11):
#         f.write(f"this is line {i}\n")


# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

#     Read the file line by line
#     Read only the 5th line of the file
#     Read only the 5 first characters of the file
#     Read all the file and return it as a list of strings. Then split each word
#     Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
#     Append your first name at the end of the file
#     Append "SkyWalker" next to each first name "Luke"

#     Read the file line by line
with open(r'sample.txt', 'r', encoding= 'utf-8') as file:
    list_content = file.readlines()
    for line in list_content:
        print(line)

# #     Read only the 5th line of the file
# print("\n--- Ahora vamos a leer la quinta línea ---\n")

# # Segundo bloque: leer específicamente la quinta línea
# with open(r'sample.txt', 'r', encoding='utf-8') as file:
#     # Saltamos las primeras 4 líneas
#     for _ in range(4):
#         next(file)
    
#     # Leemos la quinta línea
#     line = file.readline()
#     print("La quinta línea es:", line if line else "El archivo no tiene 5 líneas")


# #     Read only the 5 first characters of the file
# with open(r'sample.txt', 'r', encoding= 'utf-8') as file:


# ex2
    print("5th line:", list_content[4])

# ex3
    file.seek(0)
    char = file.readline(4)
    print(char)

# ex4
    print(list_content)
    for line in list_content:
        print(list(line))

# ex5
    occurences = {"Darth": 0, "Lea": 0, "Luke": 0}
    for line in list_content:
        if line == "Darth\n":
            occurences["Darth"] += 1
        if line == "Lea\n":
            occurences["Lea"] += 1
        if line == "Luke\n":
            occurences["Luke"] += 1
    print(occurences)

# ex6