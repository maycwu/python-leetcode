# You are given a string s consisting of only uppercase english characters and an integer k.
# You can choose up to k characters of the string and replace them with any other uppercase English character.
#
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
#
# Example 1:
# Input: s = "XYYX", k = 2
# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
#
# Example 2:
# Input: s = "AAABABB", k = 1
# Output: 5

# {'a': 2, 'b': 1, 'c': 2}
# window = 'aabcc' -> 5
# max_key = 2
# 3 - 2 = 1 <= k? yes
# update result length with window size
#
# 5 - 2 = 3 <= k? no
# move left pointer by 1
# decrement window
#
# {'a': 1, 'b': 1, 'c': 2}
# window = 'abcc' -> 4

def characterReplacement(s, k):
    left = 0  # Left boundary of the sliding window
    result = 0  # Stores the maximum length of valid substring found
    map = {}  # Tracks frequency of each character in current window

    # Expand the window by moving the right pointer
    for right in range(len(s)):
        char = s[right]
        # Note: Using string slicing here would be O(n) per operation
        # window = s[left: right+1]  # Avoid this for better performance

        # Current window size (from left to right, inclusive)
        window_size = right - left + 1
        
        # Update frequency of current character
        map[char] = map.get(char, 0) + 1

        # Find the character with highest frequency in current window
        # Example: {'a': 2, 'b': 3, 'c': 2} -> returns 'b'
        max_key = max(map, key=map.get)

        # Check if we can replace other characters to make all same
        # (window_size - count of most frequent char) = chars to replace
        if (window_size - map[max_key]) <= k:
            # Valid window - update result if this is the largest valid window found
            result = max(result, window_size)
        else:
            # Invalid window - move left pointer to shrink window
            map[s[left]] -= 1  # Remove leftmost character from current window
            left += 1  # Slide window right

    return result  # Return length of longest valid substring


# Test Case 1: Example from problem description
print(characterReplacement("aabccbb", 2))  # Output: 5 (Replace 'c's with 'b's: "aabbbbb")

# Test Case 2: Example from problem description
print(characterReplacement("XYYX", 2))  # Output: 4 (Replace both 'X's with 'Y's or vice versa)

# Test Case 3: Example from problem description
print(characterReplacement("AAABABB", 1))  # Output: 5 (Replace 'B' at index 5 with 'A')

# Test Case 4: All characters same, no replacement needed
print(characterReplacement("AAAAA", 2))  # Output: 5 (No replacement needed)

# Test Case 5: Empty string
print(characterReplacement("", 2))  # Output: 0

# Test Case 6: Single character string
print(characterReplacement("A", 1))  # Output: 1

# Test Case 7: All characters different, k=1
print(characterReplacement("ABCDE", 1))  # Output: 2 (Can replace any one character)

# Test Case 8: Need to replace all characters
print(characterReplacement("ABCDE", 5))  # Output: 5 (Can replace all characters to make them same)

# Test Case 9: Alternating characters with k=1
print(characterReplacement("ABAB", 1))  # Output: 3 (Replace one 'A' or 'B')

# Test Case 10: Large k value
print(characterReplacement("AABABBA", 10))  # Output: 7 (Can replace all if needed)

# Test Case 11: k=0, find longest existing run of same characters
print(characterReplacement("AABBBCCCCDD", 0))  # Output: 4 (Longest run is 'CCCC')

# Test Case 12: All characters same except one at the end
print(characterReplacement("AAAAAB", 1))  # Output: 6 (Replace 'B' with 'A')

# Test Case 13: All characters same except one in the middle
print(characterReplacement("AAABAAA", 1))  # Output: 7 (Replace 'B' with 'A')
