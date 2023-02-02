import re
import os
from MinimumEditDistance import MinimumEditDistance

class SpellChecker():
    user_input = str()
    console_msg_welcome = str()
    console_msg_seek_inp = str()
    words = list()
    PUNCTUATIONS = None
    DICTIONARY = dict()
    errors = None
    med = None
    Sugesstions = None
    garbage_strings = list()

    def __init__(self) -> None:
        self.user_input = None
        
        self.console_msg_welcome ="""
            --------------------------------------------------------------------------------------------
                                Welcome to Spell Checker by Khurdula, Harsha Vardhan!
            Please enter a text to check for spell errors, or enter phrase 'quit' to exit the program."
            --------------------------------------------------------------------------------------------
        """
        self.console_msg_seek_inp = """----------------------------\nEnter text to be checked: """
        self.PUNCTUATIONS =  "[\!\(\)\-\[\]\{\}\;\:\'\"\,\<\>\.\/\?\@\#\$\%\^\&\*\_\~\']"
        self.build_dictionary()
        self.errors = list()
        self.Sugesstions = dict()

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
            
            return [ x for x in temp.values() ]

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
            
            has_errors = False
            for word in self.words:
                if self.DICTIONARY.get(word, None) is None:
                    has_errors = True
                    self.errors.append(word)
                    self.Sugesstions[word] = list()
                else:
                    continue           
            return has_errors
        
        except Exception as e:
            print("The following error occured while trying to check user input for errors: " + str(e))

    def reset_suggestions(self) -> None:
        """
        Suggestions might contain corrections from previously entered text, which has to be discarded for current input.
        """
        try:
            self.Sugesstions.clear()
        except Exception as e:
            print(str(e))

    def make_suggestions(self) -> None:
        """
        make_suggestions aims to build a list of suggested words that are misspelt or unavailable in our Dictionary.
        This is achieved by using MinimumEditDictance algorithm.
        """

        try:
            for word in self.errors:
                for possible_correction in self.DICTIONARY.keys():
                    if len(word) == 1:
                        self.Sugesstions[word] = ['i', 'a']
                    elif possible_correction.startswith(word[0]):
                        temporary_object = MinimumEditDistance(word, possible_correction)
                        cost = temporary_object.compute_distance()
                        
                        if cost<= (len(word)/1.5):
                            #print(word, possible_correction, str(cost))
                            if self.Sugesstions.get(word, None) is None:
                                print(word)
                                raise TypeError("Suggestions failed to store the possible corrections.")
                            else:
                                self.Sugesstions[word].append(possible_correction)
            
            self.garbage_strings.clear()
            print("""\nMisspelling - Suggestion(s)
--------------------------------""")
            #print(self.Sugesstions)
            for word in self.errors:
                suggestions = ", ".join(self.Sugesstions.get(word))
                if len(suggestions.strip()) == 0:
                    self.garbage_strings.append(word)
                else:
                    print("\n" + word + " - " + suggestions)
            if len(self.garbage_strings) != 0:
                print("Garbage strings, that were identified within total session: " + ", ".join(self.garbage_strings))

        except Exception as e:
            print(e)
        
    def spell_checker(self) -> None:
        """
        The main method, that begins the execution of the SpellChecker's main functionalities.
        """

        print(self.console_msg_welcome)

        while self.user_input != "quit":
            self.user_input = input(self.console_msg_seek_inp)
            self.normalize_input() #normalizes the input text, and tokenizes it.
            self.Sugesstions.clear() #clears previous suggestions stored.
            self.errors.clear() #clears previous errors that were identified.
            has_errors = self.check_for_errors() #checks for words that are not in DICTIONARY.

            if has_errors is True: #check if user input has any input that has errors.
                self.make_suggestions()
            else:
                print("No misspellings detected!")
        print("Goodbye!")

obj = SpellChecker()
obj.spell_checker()
