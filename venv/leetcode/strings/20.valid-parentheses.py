# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

str = "{}[]{}"
str2 = "{)"
str3 = "((()))"


# def isValid(str):
#     stack = []  # only use append and pop
#     pairs = {
#         '(': ')',
#         '{': '}',
#         '[': ']'
#     }
#     for bracket in str:
#         if bracket in pairs:
#             stack.append(bracket)
#         elif len(stack) == 0 or bracket != pairs[stack.pop()]:
#             return False
#
#     return len(stack) == 0

def isValid(s):
    if len(s) == 1:
        return False

    stack = []  # only use append and pop

    pairs = {"(": ")", "{": "}", "[": "]"}
    for bracket in s:
        # if curr bracket is an opening bracket then append to stack and continue on
        if bracket in pairs:
            stack.append(bracket)
            continue
        # if curr bracket does not match with opening bracket in the stack, then it is not valid
        # if curr bracket is not an opening bracket then its not a valid parentheses by default
        elif len(stack) == 0 or bracket != pairs[stack[-1]]:
            return False
        # if curr bracket matches with an opening bracket in the stack, then remove it from stack
        elif bracket == pairs[stack[-1]]:
            stack.pop()

    if len(stack) == 0:
        return True


print(isValid(str))
