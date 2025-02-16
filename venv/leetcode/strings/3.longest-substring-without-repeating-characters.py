# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# def lengthOfLongestSubstring(str):
#     if len(str) == 0:
#         return 0
#
#     window_start = 0
#     longest = 0
#     window_length = 0
#
#     last_seen_at = {}
#
#     for index, val in enumerate(str):
#         if val not in last_seen_at:
#             last_seen_at[val] = index
#         else:
#             if last_seen_at[val] >= window_start:
#                 window_length = index - window_start
#                 if longest < window_length:
#                     longest = window_length
#                 window_start = last_seen_at[val] + 1
#
#             last_seen_at[val] = index
#
#     index += 1
#
#     if longest < index - window_start:
#         longest = index - window_start
#
#     return longest

def lengthOfLongestSubstring(str):
    # Sets cannot contain duplicates
    charSet = set()

    # Pointers for sliding window
    left = 0
    result = 0

    for right in range(len(str)):
        while str[right] in charSet:
            charSet.remove(str[left])
            left += 1

        charSet.add(str[right])
        result = max(result, right - left + 1)

    return result




print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbb"))
print(lengthOfLongestSubstring("pwwkew"))