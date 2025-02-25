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