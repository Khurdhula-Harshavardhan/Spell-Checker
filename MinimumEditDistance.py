

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

    def show_table(self):
        for row in self.table:
            print(row, end= "\n")

    def compute_distance(self) -> int():
        """
        MinimumEditDistance.compute_distance() has the primary objective or determining minimum number of edits,
        or changes that are to be done, inorder to transform first_string into second_string.
        This is done by using the following methods:
        """
        

        for i in range(1,self.string_one_length+1):
            for j in range(1,self.string_two_length+1):
                

                if self.first_string[i-1] == self.second_string[j-1]:
                    value = self.table[i-1][j-1]
                else:
                    value = min(self.table[i-1][j]+1, self.table[i][j-1]+1, self.table[i-1][j-1]+2)
                self.table[i][j] = value
                
            
        self.show_table()
        return self.table[i][j]


obj = MinimumEditDistance("rain", "gain")
print(obj.compute_distance())



 