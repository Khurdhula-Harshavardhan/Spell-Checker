import re
class SpellChecker():
    user_input = str()
    console_msg_welcome = str()
    console_msg_seek_inp = str()
    words = list()
    PUNCTUATIONS = None

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

    def normalize_input(self):
        """
        Normalize_input() method aims normalize user input,
        for proper spell check. This is done in a linear fashion:
        """
        self.user_input = self.user_input.lower() #lowers all the text for case consistency.
        self.user_input = re.sub(self.PUNCTUATIONS, '', self.user_input) #remove all punctuations.
        print(self.user_input)
        self.words = re.findall("[a-z]+", self.user_input) #capture all words in a list. aka Tokenize.
        print(self.words)

    def spell_checker(self):
        print(self.console_msg_welcome)
        while self.user_input != "quit":
            self.user_input = input(self.console_msg_seek_inp)
            self.normalize_input()
        print("Goodbye!")
obj = SpellChecker()
obj.console()
