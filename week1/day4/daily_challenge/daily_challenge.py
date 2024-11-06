# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column,
# selecting only the alpha characters and connecting them. Then he replaces every group of symbols between
# two alpha characters by a space.

string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# first we split the string as a list of lists
matrix = [list(line) for line in string.split("\n")]
print(f"the matrix is {matrix}")

# matrix = []
# for line in string.split("\n"):
#     matrix.append(list(line))
# print(matrix)

# now we swep with a fixed index (column) through the lines (rows) 
print("It can be waaay easier with a dataframe... anyway :( aaaagrfgfgfeeghiuhna!!!!!")

# matrix dimensions:
rows = len(matrix)
print(f"rows number: {rows}")
cols = len(matrix[0])
print(f"cols number: {cols}")

message = []
for col in range(cols):
    symbol_counter = 0 # instantiate the symbols counter
    
    for row in range(rows):
        char = matrix[row][col] # fixed row

        if symbol_counter == 2: # if the counter reached 2, it is reseted
            message.append(" ")
            symbol_counter = 0
        
        if char.isalpha() or (char == " "):
            message.append(char)
        else:
            symbol_counter += 1

        """I dont know why cant reset the counter at the end and have to do it at the beggining!!!"""
        # if symbolCounter == 2:
        #     message.append(" ")
        #     symbolCounter = 0

print()
print("".join(message))