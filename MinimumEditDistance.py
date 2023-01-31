

class MinimumEditDistance():
    string_one_length = int()
    string_two_length = int()
    first_string = str()
    second_string = str()

    table = list()

    """
    Constructor, to set up global attributes.
    """
    def __init__(self, first_string, second_string) -> None:
        """
        This is a parameterized constructor that takes 2 arguements, the words themselves.
        This constructor sets up all the attributes of the class, that are used through out to computer the
        minimum edit distance.
        """
        self.string_one_length = len(first_string)
        self.string_two_length = len(second_string)
        self.first_string = first_string
        self.second_string = second_string

        #creates a two dimensional list for storing the table values. 
        self.table = [[0 for i in range(self.string_two_length + 1)] for j in range(self.string_one_length + 1)]

        #creates a skeleton table, with values that are initialized for further processing.
        for i in range(self.string_one_length+1):
            for j in range(self.string_two_length+1):

                if i == 0:
                    self.table[i][j] = j
                elif j==0:
                    self.table[i][j] = i



    def compute_distance(self) -> int():
        """
        MinimumEditDistance.compute_distance() has the primary objective or determining minimum number of edits,
        or changes that are to be done, inorder to transform first_string into second_string.
        This is done by using the following methods:
        """
        print(self.table)


obj = MinimumEditDistance("Harsha", "Vardhan")
obj.compute_distance()



 