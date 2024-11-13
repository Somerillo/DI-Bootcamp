
#     OOP
#     Modules


# Instructions :

# The goal of the exercise is to create a class that will help you analyze a specific text.
# A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.


# Part I

# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

#     Create a class called Text that takes a string as an argument and store the text in a attribute.
#     Hint: You need to manually copy-paste the text, straight into the code

#     Implement the following methods:
#         a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
#         a method that returns the most common word in the text.
#         a method that returns a list of all the unique words in the text.


class Text:
    def __init__(self, text_input):
        """
        takes a string as an argument and store the text in a attribute\n
        Hint: You need to manually copy-paste the text, straight into the code
        """
        # in lower bc Upper_word = lower_word
        self.text_input = text_input.lower()
        # to count te words in the text we must split it and separated by a space " "
        self.words = self.text_input.split()

    def frequency_word(self, word):
        """
        a method to return the frequency of a word in the text
        """
        word = word.lower()
        freq = self.words.count(word)
        if freq == 0:
            return None
        else:
            return freq

    def commonest_word(self):
        """
        a method that returns the most common word in the text.
        """
        if not self.words:
            return "the text is as empty as the meaning of studying OOP for DA :)"
        else:
            # Find the most common word by getting the maximum of the unique words,
            # using the count of each word in the original list as the comparison key
            return max(set(self.words), key=self.words.count)
        
    def unique_words(self):
        """
        a method that returns a list of all the unique words in the text
        """
        if not self.words:
            return "the text is as empty as the meaning of studying OOP for DA :)"
        else:
            return list(set(self.words))
        
string = "A good book would sometimes cost as much as a good house."

print("------------------------------------ Part I ------------------------------------")
print(Text(string).frequency_word("")) # None
print(Text(string).frequency_word("a")) # 2
print(Text(string).commonest_word()) # "a" is the first repeating 2 times
print(Text(string).unique_words())


# Part II

# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

#     Implement a classmethod that returns a Text instance but with a text file:

#         >>> Text.from_file('the_stranger.txt')

#     Hint: You need to open and read the text from the text file. (middel shock)

#     Now, use the provided the_stranger.txt file and try using the class you created above.

class Text:
    def __init__(self, text_input):
        """
        takes a string as an argument and store the text in a attribute\n
        Hint: You need to manually copy-paste the text, straight into the code
        """
        # in lower bc Upper_word = lower_word
        self.text_input = text_input.lower()
        # to count te words in the text we must split it and separated by a space " "
        self.words = self.text_input.split()

    @classmethod
    def from_file(cls, file_name): # class & file name
        """
        creates an instance of the class Text from a text file
        """
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            return f"{file_name} not found"

    def frequency_word(self, word):
        """
        a method to return the frequency of a word in the text
        """
        word = word.lower()
        freq = self.words.count(word)
        if freq == 0:
            return None
        else:
            return freq

    def commonest_word(self):
        """
        a method that returns the most common word in the text.
        """
        if not self.words:
            return "the text is as empty as the meaning of studying OOP for DA :)"
        else:
            # Find the most common word by getting the maximum of the unique words,
            # using the count of each word in the original list as the comparison key
            return max(set(self.words), key=self.words.count)
        
    def unique_words(self):
        """
        a method that returns a list of all the unique words in the text
        """
        if not self.words:
            return "the text is as empty as the meaning of studying OOP for DA :)"
        else:
            return list(set(self.words))
        
print("\n\n------------------------------------ Part II ------------------------------------")
analysis = Text.from_file("the_stranger.txt")
if isinstance(analysis, Text):
    print(analysis.frequency_word("supa;k;dfnvoaamvercali")) # None
    print(analysis.commonest_word())
    print(analysis.frequency_word("the"))
    print(len(analysis.unique_words())) # we dont need to print the whole words list i think