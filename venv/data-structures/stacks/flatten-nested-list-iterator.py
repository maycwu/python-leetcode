class NestedIterator:

    # NestedIterator constructor initializes the stack using the
    # given nested_list list
    def __init__(self, nested_list):
        self.nested_list_stack = list(reversed([NestedIntegers(val) for val in nested_list]))

    # has_next() will return True if there are still some integers in the
    # stack (that has nested_list elements) and, otherwise, will return False.
    def has_next(self):
        while len(self.nested_list_stack) > 0:
            top = self.nested_list_stack[-1]
            if top.is_integer():
                return True

            top_list = self.nested_list_stack.pop().get_list()

            i = len(top_list) - 1
            while i >= 0:
                self.nested_list_stack.append(top_list[i])
                i -= 1
        return False

    # next will return the integer from the nested_list
    def next(self):
        if self.has_next():
            return self.nested_list_stack.pop().get_integer()
        return None

def create_nested_iterator_structure(input_list):
    def parse_input(nested, input_list):
        if isinstance(input_list, int):
            nested.set_integer(input_list)
        else:
            for item in input_list:
                child = NestedIntegers()
                nested.add(child)
                parse_input(child, item)

    nested_structure = NestedIntegers()
    parse_input(nested_structure, input_list)
    return nested_structure

def create_nested_iterator_from_structure(nested_structure):
    def flatten(nested, result):
        if nested.is_integer():
            result.append(nested.get_integer())
        else:
            for child in nested.get_list():
                flatten(child, result)

    flattened_list = []
    flatten(nested_structure, flattened_list)
    return NestedIterator(flattened_list)

# Helper function
class NestedIntegers:
    # Constructor initializes a single integer if a value has been passed
    # else it initializes an empty list
    def __init__(self, integer=None):
        if integer:
            self.integer = integer
        else:
            self.n_list = []
            self.integer = 0

            # If this NestedIntegers holds a single integer rather
    # than a nested list, returns TRUE, else, returns FALSE
    def is_integer(self):
        if self.integer:
            return True
        return False

    # Returns the single integer, if this NestedIntegers holds a single integer
    # Returns null if this NestedIntegers holds a nested list
    def get_integer(self):
        return self.integer

    #  Sets this NestedIntegers to hold a single integer.
    def set_integer(self, value):
        self.n_list = None
        self.integer = value

    # Sets this NestedIntegers to hold a nested list and adds a nested
    # integer to it.
    def add(self, ni):
        if self.integer:
            self.n_list = []
            self.n_list.append(NestedIntegers(self.integer))
            self.integer = None
        self.n_list.append(ni)

        # Returns the nested list, if this NestedIntegers holds a nested list
    # Returns null if this NestedIntegers holds a single integer
    def get_list(self):
        return self.n_list


# Driver code
def main():

    inputs = [
        [1, [2, 3], 4],
        [3, [2, 3, 4], 4, [2, 3]],
        [[2, 3], 3, [2, 3], 4, [2, 3, 4, 5]],
        [1, [3, [4, [5, 6], 7], 8], 9],
        [[2, 3, [2, 3]]]
    ]

    for i, test_case_input in enumerate(inputs, start=1):
        print(i, ".\tOriginal structure: ", inputs[i-1], sep="")
        print("\n\tOutput:\n")
        nested_structure = create_nested_iterator_structure(test_case_input)
        test_case = create_nested_iterator_from_structure(nested_structure)

        #result = []
        while test_case.has_next():
            print("\titr.next(): ", test_case.next())

        print("-"*100)

if __name__ == '__main__':
    main()


