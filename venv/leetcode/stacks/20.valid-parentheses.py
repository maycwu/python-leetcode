def isValid(s: str) -> bool:
    if len(s) <= 1:
        return False

    result = []

    #valid pairs dictionary
    pairs = {
        "[" : "]",
        "{" : "}",
        "(" : ")"
    }

    for char in s:
        # ensures the stack is not empty before accessing result[-1]
        if result and result[-1] == char:
            result.pop()
        else:
            # appends the closing bracket, if open bracket, then appends "None"
            result.append(pairs.get(char))

    if len(result) == 0:
        return True
    else:
        return False

print(isValid("(())"))


"""
20. Valid Parentheses (Easy)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    pass

# Test cases
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("[", False),
    ("", True)
]

for s, expected in test_cases:
    result = isValid(s)
    print(f'Input: "{s}"')
    print(f'Output: {result}')
    print(f'Expected: {expected}')
    print(f'{"✅" if result == expected else "❌"}')
    print()