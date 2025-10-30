# Problem: Find the length of the longest substring without repeating characters.
#
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


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbb"))
print(lengthOfLongestSubstring("pwwkew"))

"""
Visual Example: Sliding Window Approach

Input: s = "abcabcbb"

Iteration 1: 'a'        | [a]bcabcbb  | longest = 1  | last_seen = {'a': 0}
Iteration 2: 'b'        | [ab]cabcbb  | longest = 2  | last_seen = {'a':0, 'b':1}
Iteration 3: 'c'        | [abc]abcbb  | longest = 3  | last_seen = {'a':0, 'b':1, 'c':2}
Iteration 4: 'a' (dup)  | a[bca]bcbb  | longest = 3  | last_seen = {'a':3, 'b':1, 'c':2}
Iteration 5: 'b' (dup)  | ab[cab]cbb  | longest = 3  | last_seen = {'a':3, 'b':4, 'c':2}
Iteration 6: 'c' (dup)  | abc[abc]bb  | longest = 3  | last_seen = {'a':3, 'b':4, 'c':5}
Iteration 7: 'b' (dup)  | abca[bc]bb  | longest = 3  | last_seen = {'a':3, 'b':6, 'c':5}
Iteration 8: 'b' (dup)  | abcab[cb]b  | longest = 3  | last_seen = {'a':3, 'b':7, 'c':5}

Final Output: 3 ("abc" or "bca" or "cab")
"""


# with dictionary
# Efficiency: Dictionary is more efficient as it allows direct jumps instead of removing one by one
def find_longest_substring(s):
    # Handle empty string case
    if not s:
        return 0

    # Dictionary to store the last seen index of each character
    last_seen = {}  # Format: {character: last_seen_index}

    # Initialize sliding window pointers and result
    start = 0  # Left boundary of current window
    longest = 0  # Tracks maximum length found so far

    # Iterate through the string with right pointer (i)
    for i in range(len(s)):
        ch = s[i]

        # If character is in current window (duplicate found)
        # last_seen[ch] >= start ensures we only consider duplicates within current window
        if ch in last_seen and last_seen[ch] >= start:
            # Move start to right after the previous occurrence of current character
            # This ensures no duplicates in the new window
            start = last_seen[ch] + 1

        # Update the last seen index of current character
        last_seen[ch] = i

        # Calculate current window size and update maximum length
        # i - start + 1 = length of current valid window
        longest = max(longest, i - start + 1)
    return longest


print(find_longest_substring("abcabcbb"))  # Output: 3
print(find_longest_substring("bbbb"))  # Output: 1
print(find_longest_substring("pwwkew"))  # Output: 3
