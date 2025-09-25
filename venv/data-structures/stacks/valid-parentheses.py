# Statement
# Given a string that may consist of opening and closing parentheses, your task is to check whether or not the string contains valid parenthesization.
#
# The conditions to validate are as follows:
#
# Every opening parenthesis should be closed by the same kind of parenthesis. Therefore, {)and [(]) strings are invalid.
#
# Every opening parenthesis must be closed in the correct order. Therefore, )( and ()(() are invalid.

# Example 1: (){[{()}]}
# Output: TRUE

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        brackets = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
        stack = []

        for bracket in s:
            # Opening bracket → push its expected closing bracket
            if bracket in brackets:
                stack.append(brackets[bracket])

            # Closing bracket → check if it matches the top of the stack
            elif stack and stack[-1] == bracket:
                stack.pop()

            else:
                return False  # mismatch or no opening bracket for this closing one
        return len(stack) == 0


sol = Solution()
# print(sol.isValid("([{}])"))
# print(sol.isValid("(){[{()}]}"))
print(sol.isValid("()]"))
