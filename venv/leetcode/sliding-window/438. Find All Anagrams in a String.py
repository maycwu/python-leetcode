from collections import defaultdict, Counter

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

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

"""
Find All Anagrams in a String - Visual Explanation

Problem: Given two strings s and p, return all start indices of p's anagrams in s.

Example:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]

Visual Walkthrough:

Initial State:
- s = "c b a e b a b a c d"
  Indices:0 1 2 3 4 5 6 7 8 9
- p = "a b c"
- p_count = {'a':1, 'b':1, 'c':1}  # Character counts we need to match
- window_size = len(p) = 3
- result = []

Step 1: Window [0,2] "cba"
- Current window: "cba"
- Current counts: {'c':1, 'b':1, 'a':1}
- Matches p_count? Yes → Add index 0 to result
- result = [0]

Step 2: Window [1,3] "bae"
- Current window: "bae"
- Current counts: {'b':1, 'a':1, 'e':1}
- 'e' not in p_count → No match
- result remains [0]

Step 3: Window [2,4] "aeb"
- Current window: "aeb"
- Current counts: {'a':1, 'e':1, 'b':1}
- 'e' not in p_count → No match
- result remains [0]

... (sliding window continues)

Step 7: Window [6,8] "bac"
- Current window: "bac"
- Current counts: {'b':1, 'a':1, 'c':1}
- Matches p_count? Yes → Add index 6 to result
- result = [0, 6]

Final result: [0, 6]
"""


def findAnagrams(s, p):
    result = []
    p_count = Counter(p)

    # Initialize first window
    window_count = Counter(s[:len(p)])

    # check first window
    if window_count == p_count:
        result.append(0)

    # slide the window
    for i in range(1, len(s) - len(p) + 1):
        # remove the leftmost character of the window
        left_char = s[i - 1]
        if window_count[left_char] == 1:
            del window_count[left_char]
        else:
            window_count[left_char] -= 1

        # Add the new right character
        right_char = s[i + len(p) - 1]
        window_count[right_char] = window_count.get(right_char, 0) + 1

        # Check if current window matches p's character counts
        if window_count == p_count:
            result.append(i)
    return result


# Test cases
test_cases = [
    ("cbaebabacd", "abc"),  # Expected: [0, 6]
    ("abab", "ab"),  # Expected: [0, 1, 2]
    ("aaaaaaaaaa", "a"),  # Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ("abc", "d"),  # Expected: []
]

for s, p in test_cases:
    print(f"\nInput: s = \"{s}\", p = \"{p}\"")
    result = findAnagrams(s, p)
    print(f"Output: {result}")

    # Print visualization for the first test case
    if s == "cbaebabacd" and p == "abc":
        print("\nDetailed Visualization:")
        p_count = Counter(p)
        window_count = Counter()
        result = []

        # Initial window
        print("\nInitial Window:")
        for i in range(len(p)):
            char = s[i]
            if char in p_count:
                window_count[char] += 1
            print(f"  Add '{char}': {window_count}")

        if window_count == p_count:
            result.append(0)
            print(f"Found anagram at index 0: {s[0:len(p)]}")

        # Sliding window
        print("\nSliding Window:")
        for i in range(len(p), len(s)):
            # Remove left character
            left_char = s[i - len(p)]
            if left_char in window_count:
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
                print(f"  Remove '{left_char}': {window_count}")

            # Add new character
            right_char = s[i]
            if right_char in p_count:
                window_count[right_char] += 1
                print(f"  Add '{right_char}': {window_count}")

            # Check for anagram
            if window_count == p_count:
                start_idx = i - len(p) + 1
                result.append(start_idx)
                print(f"  Found anagram at index {start_idx}: {s[start_idx:start_idx + len(p)]}")

print(findAnagrams("ababababab", "aab"))  # Output: [0,2,4,6]
print(findAnagrams("cbaebabacd", "abc"))  # Output: [0,6]
print(findAnagrams("abab", "ab"))  # Output: [0,1,2]
