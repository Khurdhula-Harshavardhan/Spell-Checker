import re
import os
class SpellChecker():
    user_input = str()
    console_msg_welcome = str()
    console_msg_seek_inp = str()
    words = list()
    PUNCTUATIONS = None
    DICTIONARY = dict()
    errors = None

    def __init__(self) -> None:
        self.user_input = None
        
        self.console_msg_welcome ="""
            --------------------------------------------------------------------------------------------
                                Welcome to Spell Checker by Khurdula, Harsha Vardhan!
            Please enter a text to check for spell errors, or enter phrase 'quit' to exit the program."
            --------------------------------------------------------------------------------------------
        """
        self.console_msg_seek_inp = "Enter text to be checked: "
        self.PUNCTUATIONS =  "[\!\(\)\-\[\]\{\}\;\:\'\"\,\<\>\.\/\?\@\#\$\%\^\&\*\_\~\']"
        self.build_dictionary()
        self.errors = list()

    def build_dictionary(self) -> None:
        """
        This method is called by the constructor to build the dictionary that shall contain
        all the words, these words are collected from dictionary.txt
        """
        try:
            file_handler = open(os.getcwd() + "/dictionary.txt","r", encoding= "UTF-8")
            words = file_handler.readlines()

            for word in words:
                word  = re.sub("\n", "", word)
                self.DICTIONARY[word] = word
        except Exception as e:
            print(e)


    def remove_duplicates(self, words) -> list():
        """
        Remove_duplicates, is primarily used to discard the repeated tokens in stream of words.
        This is achived by using a map to iterate and store only newly occuring words.
        """
        try:
            temp = dict()

            for word in words:
                if temp.get(word, None) is None:
                    temp[word] = word
                else:
                    continue

            return list(temp.keys())

        except Exception as e:
            print("The following error occured while trying to remove duplicates from user input: " + str(e))

    def normalize_input(self) -> None:
        """
        Normalize_input() method aims normalize user input,
        for proper spell check. This is done in a linear fashion:
        """
        try:
            self.user_input = self.user_input.lower() #lowers all the text for case consistency.
            self.user_input = re.sub(self.PUNCTUATIONS, '', self.user_input) #remove all punctuations.
            self.words = re.findall("[a-z]+", self.user_input) #capture all words in a list. aka Tokenize.
            self.words = self.remove_duplicates(self.words) #discard duplicate words.
        except Exception as e:
            print("The following error occured while trying to Normalize user input: " + str(e))
    
    def check_for_errors(self) -> bool:
        """
        check_for_errors, determines if the text given as input from the user has any
        token that is not present in our Dictionary.
        Note: in this scenario, any word that is not part of our vocabulary can be called as an mispelt word / error.
        it returns True if the user input contains an error, false otherwise.
        """
        try:
            for word in self.words:
                if self.DICTIONARY.get(word, None) is None:
                    self.errors.append(word)
                    return True
                else:
                    continue

            return False
        
        except Exception as e:
            print("The following error occured while trying to check user input for errors: " + str(e))
        
    def spell_checker(self) -> None:
        print(self.console_msg_welcome)
        while self.user_input != "quit":
            self.user_input = input(self.console_msg_seek_inp)
            self.normalize_input() #normalizes the input text, and tokenizes it.
            has_errors = self.check_for_errors() #checks for words that are not in DICTIONARY.

            if has_errors is True:
                print("User input has errors: ")
                print(self.errors)
                self.make_suggestions()
            else:
                print("No misspellings detected!")
        print("Goodbye!")

obj = SpellChecker()
obj.spell_checker()
