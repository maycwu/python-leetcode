def reverseWords(s):
    words = s.split()
    res = []

    for i in range(len(words) - 1, -1, -1):
        res.append(words[i])
        if i != 0:
             res.append(" ")
    return "".join(res)


# def reverseWords(self, s: string) -> string:
#     words = s.split()
#     words.reverse()
#     reversed_s = ' '.join(words)
#     return reversed_s

def main():
    string_to_reverse = ["Hello      World",
                         "a   string   with   multiple   spaces",
                         "Case Sensitive Test Case 1234",
                         "a 1 b 2 c 3 d 4 e 5",
                         "     trailing spaces",
                         "case test interesting an is this"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\tOriginal string: '" + "".join(string_to_reverse[i]), "'", sep='')
        result = reverseWords(string_to_reverse[i])

        print("\tReversed string: '" + "".join(result), "'", sep='')
        print("-" * 100)


if __name__ == '__main__':
    main()