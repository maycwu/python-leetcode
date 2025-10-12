
def permute_word(word):
    def backtrack(current, remaining):
        if not remaining:
            result.append(current)
            return
        for i in range(len(remaining)):
            # Choose the current character
            next_char = remaining[i]
            # Remove it from remaining characters
            # remaining[:0] = ""
            # remaining[0+1:] = "ab"
            new_remaining = remaining[:i] + remaining[i+1:]
            # Recurse with the chosen character added to current
            backtrack(current + next_char, new_remaining)

    result = []
    backtrack("", word)
    return result

# Driver code
def main():
    input_word = ["bad"]

    for index in range(len(input_word)):
        permuted_words = permute_word(input_word[index])

        print(index + 1, ".\t Input string: '", input_word[index], "'", sep="")
        print("\t All possible permutations are: ",
              "[", ', '.join(permuted_words), "]", sep="")
        print('-' * 100)


if __name__ == '__main__':
    main()
