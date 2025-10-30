"""
Medium

A permutation is a rearrangement of all the elements in a set into a particular order. In the context of strings, it means all possible ways to arrange the characters of the string.

Key Points About Permutations:
Same Characters, Different Orders:
For the string "abc", the permutations are:
abc, acb, bac, bca, cab, cba
All permutations contain the same characters, just in different orders.

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Approach:
1. Sliding Window with Frequency Count
   - Use a fixed-size window of length s1
   - Compare frequency of characters in window with s1's frequency
   - Slide the window through s2 and check for matches

Time Complexity: O(n + m) where n is length of s1 and m is length of s2
Space Complexity: O(1) - using fixed size arrays
"""


"""
Visual Walkthrough for s1 = "ab", s2 = "eidbaooo":

Initial Setup:
s1 = "ab" (length = 2)
s2 = "e i d b a o o o"
     0 1 2 3 4 5 6 7

s1_count: [a:1, b:1, ...] (all others 0)

Window Sliding Process:

1. Window [0:2] = "ei"
   - Add 'e': window_count = [e:1, i:1]
   - Compare with s1_count: No match

2. Window [1:3] = "id"
   - Remove 'e', add 'd'
   - window_count = [d:1, i:1]
   - No match

3. Window [2:4] = "db"
   - Remove 'i', add 'b'
   - window_count = [b:1, d:1]
   - No match

4. Window [3:5] = "ba"  <-- MATCH FOUND
   - Remove 'd', add 'a'
   - window_count = [a:1, b:1]
   - MATCHES s1_count [a:1, b:1]
   - Return True

Visualization of Sliding Window:
e i d b a o o o
[ ]             -> "ei" (no match)
  [ ]           -> "id" (no match)
    [ ]         -> "db" (no match)
      [ ]       -> "ba" (MATCH!)

Key Points:
- Window size = len(s1)
- Update counts by removing left and adding right
- Compare frequency arrays for match
- O(n) time complexity
"""

def checkInclusion(s1: str, s2: str) -> bool:
    # Edge case: s1 is longer than s2
    if len(s1) > len(s2):
        return False

    # Initialize frequency counts for s1 and the first window in s2
    s1_count = [0] * 26
    window_count = [0] * 26

    # Populate the frequency counts
    for i in range(len(s1)):
        # Increment count for current character in s1
        s1_count[ord(s1[i]) - ord('a')] += 1
        # Increment count for current character in initial window of s2
        window_count[ord(s2[i]) - ord('a')] += 1

    # Slide the window through s2
    for i in range(len(s2) - len(s1)):
        # If frequency counts match, we found a permutation
        if s1_count == window_count:
            return True

        # Remove the leftmost character from the window
        left_char = s2[i]
        window_count[ord(left_char) - ord('a')] -= 1

        # Add the new character to the window
        right_char = s2[i + len(s1)]
        window_count[ord(right_char) - ord('a')] += 1

    # Check the last window
    return s1_count == window_count

# Brute Force Approach (for reference)
from itertools import permutations

def checkInclusion_bruteforce(s1: str, s2: str) -> bool:
    """
    Brute Force Approach:
    - Generate all permutations of s1
    - Check if any permutation is a substring of s2
    Time Complexity: O(n! * m) - Not efficient for large inputs
    """
    perms = [''.join(p) for p in permutations(s1)]
    for p in perms:
        if p in s2:
            return True
    return False

# Test cases
test_cases = [
    ("ab", "eidbaooo", True),      # "ba" is in s2
    ("ab", "eidboaoo", False),     # No permutation of "ab" in s2
    ("hello", "ooolleoooleh", False),  # Example with longer string
    ("a", "ab", True),             # Single character case
    ("adc", "dcda", True),         # Permutation at the end
    ("abc", "xyz", False),         # No match
]

for s1, s2, expected in test_cases:
    result = checkInclusion(s1, s2)
    print(f"checkInclusion('{s1}', '{s2}') -> {result} (Expected: {expected})")
    assert result == expected, f"Test failed for {s1}, {s2}"

print("\nAll test cases passed!")