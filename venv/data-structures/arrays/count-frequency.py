# def count_frequency(words):
#     count = {}
#     for word in words:
#         count[word] = count.get(word, 0) + 1
#
#     sorted_words = sorted(count.keys())
#     result = []
#     for word in sorted_words:
#         result.append(count[word])
#     return result


# print(count_frequency(["the", "dog", "got", "the", "bone"]))  # [ 1, 1, 1, 2]
# print(count_frequency(["he", "saw", "she", "saw"]))  # [1, 2, 1]


def count_freq(words):

    words.sort()
    result = []
    unique_words = set(words)
    sorted_words = sorted(list(unique_words))

    for word in sorted_words:
        result.append(words.count(word))
    return result


print(count_freq(["the", "dog", "got", "the", "bone"]))  # [ 1, 1, 1, 2]
print(count_freq(["he", "saw", "she", "saw", "abby", "abby", "abby"]))  # [1, 2, 1]
