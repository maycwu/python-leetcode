# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

from collections import Counter


def minWindow(s, t):
    req_count = Counter(t)
    window_count = {}
    result = []
    required = len(req_count)
    have = 0
    left = 0

    for right in range(len(s)):
        if s[right] in req_count:
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            if req_count[s[right]] == window_count[s[right]]:
                have += 1
            while have == required:
                result.append(s[left:right + 1])

                if s[left] in req_count:
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < req_count[s[left]]:
                        have -= 1
                left += 1
    return min(result, key=len) if result else ""

def minWindow_correct(s,t):
    req_count = Counter(t)
    window_count = {}
    result = {}
    required = len(req_count)
    have = 0
    left = 0
    min_len = float('inf')

    for right in range(len(s)):
        if s[right] in req_count:
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            if req_count[s[right]] == window_count[s[right]]:
                have += 1
            while have == required:
                # Update the result if we found a smaller window
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                if s[left] in req_count:
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < req_count[s[left]]:
                        have -= 1
                left += 1
    return result

# print(minWindow("ABDOEDECOBE", "BC"))  # Output: BANC
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: BANC
# print(minWindow("a", "a"))  # Output: a
# print(minWindow("a", "aa"))  # Output: ""
