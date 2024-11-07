# Mini-Project #2 - Hangman
# Use python to create a Hangman game.
# The computer choose a random word and mark stars for each letter of each word.
#     Then the player will guess a letter.
#         If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
#         If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
#         The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
#         The player can’t guess the same letter twice.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

print("Welcome to hangman (R)")

def draw_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    
           |
           |
           |
        """,
        """
           ------
           |    
           |    
           |
           |
           |
        """,
        """
           
           
           
           
           
           
        """
    ]
    
    return stages[6 - tries] # the original list order is inverted

tries = 0
print(draw_hangman(tries))

def map_char(word):
    long = len(word)
    dashes = ["*" for char in word]
    # dashes = "".join(dashes)
    return dashes

print("\nChoose carefully:\n")
print("".join(map_char(word)), "\n")
# print(list(word))
# print(list(enumerate(list(word))))

def game_on(tries = 0):
    list_word = list(word)
    dashes = map_char(word)

    while True:
        # dashes = map_char(dashes)
        k = 0
        char = input("Input your letter: ")
        if char in list_word:
            for i in range(len(list_word)):
                if char == list_word[i]:
                    dashes[i] = char
                    k += 1
                    
        else:
            tries += 1

        if "*" not in dashes:
            print(f"\nYou won, the word is < {word} >. Now get a life\n")
            break

        print(draw_hangman(tries))
        print("".join(dashes))

        if tries == 6:
            print("\nyou lost, get a life\n")
            break
    
game_on()