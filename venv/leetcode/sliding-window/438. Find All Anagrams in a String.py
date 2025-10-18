# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from collections import defaultdict, Counter


# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# Not an efficient solution, Counter method counts all the letters for each iteration
# resulting in time complexity O (n x m)
# def findAnagrams(s, p):
#     result = []
#     p_letters = Counter(p)
#
#     for i in range(len(s) - len(p) + 1):
#         # create a window of length p
#         sub_string = s[i:i+len(p)]
#         s_letters = Counter(sub_string)
#
#         if s_letters == p_letters:
#             result.append(i)
#     return result


def findAnagrams(s, p):
    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])

    if window_count== p_count:
        result.append(0)

    for i in range(1, len(s) - len(p) + 1):
        # remove the leftmost character of the window
        left_char = s[i-1]
        if window_count[left_char] == 1:
            del window_count[left_char]
        else:
            window_count[left_char] -= 1

        # Add the new right character
        right_char = s[i + len(p) - 1]
        window_count[right_char] = window_count.get(right_char, 0) + 1

        if window_count == p_count:
            result.append(i)

    return result

print(findAnagrams("ababababab", "aab")) # Output: [0,2,4,6]
print(findAnagrams("cbaebabacd", "abc")) # Output: [0,6]
print(findAnagrams("abab", "ab")) # Output: [0,1,2]
