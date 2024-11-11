def remove_duplicates(s):
    # Create an empty stack.
    stack = []
    # Iterate over the string
    for char in s:
        # If stack has at least one character and
        # stack's top character is same as the string's character
        if stack and stack[-1] == char:
            # Pop a character from the stack.
            stack.pop()
        else:
            # Otherwise, push that character onto the stack.
            stack.append(char)

    # Form a string from stack's elements and return that.
    return "".join(stack)


# Driver code
def main():
    inputs = ["g",
              "ggaabcdeb",
              "abbddaccaaabcd",
              "aannkwwwkkkwna",
              "abbabccblkklu"
              ]

    for i in range(len(inputs)):
        print(i + 1, ".\tRemove duplicates from string: '", inputs[i], "'", sep = "")
        resulting_string = remove_duplicates(inputs[i])
        print("\tString after removing duplicates: ", resulting_string, sep = "")
        print('-'*100)


if __name__ == "__main__":
    main()
