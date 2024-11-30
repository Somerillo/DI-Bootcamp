#ex1
with open('starwars.txt', 'r', encoding='utf-8') as file:
    list_content = file.readlines()
    for line in list_content:
        print(line)

#ex2
    print('5th line:', list_content[4])

#ex3 
    file.seek(0)
    char = file.read(3)
    print(char)

#ex4
    #list of strings:
    print(list_content)
    #Then split each word
    for line in list_content:
        print(list(line))

        
#ex5
occurences = {'Darth':0, "Lea":0, 'Luke':0}
for line in list_content:
    if line == 'Darth\n':
        occurences['Darth'] +=1
    if line == 'Lea\n':
        occurences['Lea'] +=1
    if line == 'Luke\n':
        occurences['Luke'] +=1
    
print(occurences)

#ex6


        
