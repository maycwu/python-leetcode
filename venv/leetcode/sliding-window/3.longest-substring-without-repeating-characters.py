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

# with set
def lengthOfLongestSubstring(str):
    # Sets cannot contain duplicates
    charSet = set()

    # Pointers for sliding window
    left = 0
    result = 0

    for right in range(len(str)):
        current = str[right]
        while str[right] in charSet:
            charSet.remove(str[left])
            left += 1

        charSet.add(str[right])
        result = max(result, right - left + 1)

    return result


# with dictionary
# Efficiency: Dictionary is more efficient as it allows direct jumps instead of removing one by one
def find_longest_substring(s):
    if not s:
        return 0

    last_seen = {}  # Keeps track of the last index where each character appeared
    start = 0  # Start index of the current window (substring)
    longest = 0  # Length of the longest substring found so far

    for i in range(len(s)):
        ch = s[i]
        # If we've seen this character before and it's inside the current window
        # "last_seen[ch] >= start" verifies if the character's last occurrence is within the current window (substring) we're examining.
        if ch in last_seen and last_seen[ch] >= start:
            # Move the start just past where this char was last seen
            start = last_seen[ch] + 1

        # Update the character's most recent index
        last_seen[ch] = i

        # Update the longest length found so far
        longest = max(longest, i - start + 1)

    return longest


# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbb"))
# print(lengthOfLongestSubstring("pwwkew"))

print(find_longest_substring("abcabcbb"))
print(find_longest_substring("bbbb"))
print(find_longest_substring("pwwkew"))
