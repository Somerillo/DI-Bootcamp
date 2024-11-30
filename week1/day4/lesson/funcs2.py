students = ['Leah', 'Luke', "Darth Vaider"]

def welcome():
    for index, name in enumerate(students):
        students[index] = f'Welcome {name}'
    

welcome()
print(students)

