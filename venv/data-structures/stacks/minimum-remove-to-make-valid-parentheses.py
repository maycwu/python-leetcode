#Statement

#Given a string, s, that may have matched and unmatched parentheses, remove the minimum number of parentheses
# so that the resulting string represents a valid parenthesization. For example, the string “a(b)” represents a
# valid parenthesization while the string “a(b” doesn’t, since the opening parenthesis doesn’t have any
# corresponding closing parenthesis.

#Example:
# What is the output if the following string is given as input?
#
# (((abc)(to)((q)()(
# Output: (abc)(to)(q)()



def min_remove_parentheses(s):
    stack = []
    s_list = list(s)

    for i, val in enumerate(s):
        # if stack is not empty and top element of stack is an opening parenthesis
        # and the current element is a closing parenthesis
        if len(stack) > 0 and stack[-1][0] == '(' and val == ')':
            # pop the opening parenthesis as it makes a valid pair
            # with the current closing parenthesis
            stack.pop()

        # if the current value is an opening or a closing parenthesis
        elif val == '(' or val == ')':
            # push onto stack
            stack.append([val, i])

    # Remove the invalid parentheses
    for p in stack:
        s_list[p[1]] = ""

    # convert the list to string
    result = ''.join(s_list)

    return result

# Driver code
def main():
    inputs = ["ar)ab(abc)abd(", "a)rt)lm(ikgh)", "aq)xy())qf(a(ba)q)",
              "(aw))kk())(w(aa)(bv(wt)r)",  "(qi)(kl)((y(yt))(r(q(g)s)"]
    for i in range(len(inputs)):
        print(i + 1, ". Input: \"", inputs[i], "\"", sep="")
        print("   Valid parentheses, after minimum removal: \"", \
              min_remove_parentheses(inputs[i]), "\"", sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()