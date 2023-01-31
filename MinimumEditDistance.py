

class MinimumEditDistance():
    string_one_length = int()
    string_two_length = int()
    first_string = str()
    second_string = str()

    """
    Constructor, to set up global attributes.
    """
    def __init__(self, first_string, second_string) -> None:
        self.string_one_length = len(first_string)
        self.string_two_length = len(second_string)
        self.first_string = first_string
        self.second_string = second_string


    def compute_distance(self, first_string, second_string):
        """
        MinimumEditDistance.compute_distance() has the primary objective or determining minimum number of edits,
        or changes that are to be done, inorder to transform first_string into second_string.
        This is done by using the following methods:

        """




 