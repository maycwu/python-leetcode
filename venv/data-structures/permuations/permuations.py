# This function will swap characters for every permutation
def swap_char(word, i, j):
    swap_index = list(word) # Converts "ab" to ['a', 'b']
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i]
    return ''.join(swap_index)


def permute_string_rec(word, current_index, result):
    # Prevents adding duplicate permutations
    if current_index == len(word) - 1:
        result.append(word)
        return

    for i in range(current_index, len(word)):
        # swaps character for each permutation
        swapped_str = swap_char(word, current_index, i)
        # recursively calls itself to find each permutation
        permute_string_rec(swapped_str, current_index + 1, result)

# main fuction
def permute_word(word):
    result = []

    # Starts finding permuations from start of string
    permute_string_rec(word, 0, result)
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
