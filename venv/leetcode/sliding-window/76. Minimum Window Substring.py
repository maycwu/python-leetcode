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

"""
Visual Example: Sliding Window for "ADOBECODEBANC" with t = "ABC"

Initial: left = 0, right = 0, have = 0, required = 3 (A,B,C)

Step 1: right=0 'A'  | [A]DOBECODEBANC  | have=1 (A)     | window_count={'A':1}
Step 2: right=1 'D'  | [AD]OBECODEBANC  | have=1         | window_count={'A':1}
Step 3: right=2 'O'  | [ADO]BECODEBANC  | have=1         | window_count={'A':1}
Step 4: right=3 'B'  | [ADOB]ECODEBANC  | have=2 (A,B)   | window_count={'A':1,'B':1}
Step 5: right=4 'E'  | [ADOBE]CODEBANC  | have=2         | window_count={'A':1,'B':1}
Step 6: right=5 'C'  | [ADOBEC]ODEBANC  | have=3 (A,B,C) | Found window: 'ADOBEC'
        Shrink left: left=1 'D' | A[DOBEC]ODEBANC | have=3 | window_count={'A':1,'B':1,'C':1}
        Shrink left: left=2 'O' | AD[OBEC]ODEBANC | have=3 | window_count={'A':0,'B':1,'C':1}
        ... (continue shrinking until window becomes invalid)

Final result: 'BANC' (smallest window found)
"""

"""
Visual Example: Sliding Window for "ADOBECODEBANC" with t = "ABC"

[INITIAL STATE]
- String:  A D O B E C O D E B A N C
- Indices: 0 1 2 3 4 5 6 7 8 9 10 11 12
- Target chars to find: A(1), B(1), C(1)
- required = 3 (unique characters in t)
- left = 0, right = 0, have = 0
- Current min_length = ∞
- Current min_window = ""

[EXPANSION PHASE - Move right pointer]

Step 1: right=0 'A'
- Found 'A' (needed character)
- window_count = {'A':1}
- have = 1 (found A)
- Current window: [A]DOBECODEBANC
- Have (1) < Required (3) → Continue expanding

Step 2: right=1 'D'
- 'D' not in t, skip
- Current window: [AD]OBECODEBANC
- Have remains 1

Step 3: right=2 'O'
- 'O' not in t, skip
- Current window: [ADO]BECODEBANC
- Have remains 1

Step 4: right=3 'B'
- Found 'B' (needed character)
- window_count = {'A':1, 'B':1}
- have = 2 (found A, B)
- Current window: [ADOB]ECODEBANC
- Have (2) < Required (3) → Continue expanding

Step 5: right=4 'E'
- 'E' not in t, skip
- Current window: [ADOBE]CODEBANC
- Have remains 2

Step 6: right=5 'C'
- Found 'C' (needed character)
- window_count = {'A':1, 'B':1, 'C':1}
- have = 3 (found A, B, C) → VALID WINDOW FOUND
- Current window: [ADOBEC]ODEBANC (length 6)
- New minimum window found: 'ADOBEC'
- min_length = 6, min_window = 'ADOBEC'

[SHRINKING PHASE - Try to minimize window]

Step 7: Try to shrink from left (left=0)
- Current window: [ADOBEC]ODEBANC
- Remove 'A' (left=0)
- window_count = {'A':0, 'B':1, 'C':1}
- have = 2 (removed A, now missing A)
- left = 1
- New window: A[DOBEC]ODEBANC (invalid, need A)
- Stop shrinking, need to expand right

[CONTINUE EXPANDING]

Step 8: right=6 'O' to right=9 'B'
- Expanding right until we find another 'A'
- ...

[FINAL RESULT]
- After processing entire string, smallest valid window found: 'BANC' (length 4)
- Final min_window = 'BANC'

KEY OBSERVATIONS:
1. Window expands when we don't have all required characters
2. Window contracts when we have all characters, trying to find a smaller valid window
3. We only update min_window when we find a smaller valid window
4. The algorithm ensures we find the minimum window by exploring all possibilities
"""


# Incorrect solution, need to fix
# def minWindow(s, t):
#     req_count = Counter(t)
#     window_count = {}
#     result = []
#     required = len(req_count)
#     have = 0
#     left = 0
#
#     for right in range(len(s)):
#         if s[right] in req_count:
#             window_count[s[right]] = window_count.get(s[right], 0) + 1
#             if req_count[s[right]] == window_count[s[right]]:
#                 have += 1
#             while have == required:
#                 result.append(s[left:right + 1])
#
#                 if s[left] in req_count:
#                     window_count[s[left]] -= 1
#                     if window_count[s[left]] < req_count[s[left]]:
#                         have -= 1
#                 left += 1
#     return min(result, key=len) if result else ""

# Correct
def minWindow1(s,t):
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

if __name__ == "__main__":
    # Test cases with visual output
    test_cases = [
        ("ADOBECODEBANC", "ABC"),  # Expected: "BANC"
        ("a", "a"),                # Expected: "a"
        ("a", "aa"),               # Expected: ""
        ("ABDOEDECOBE", "BC"),     # Expected: "BECOB"
        ("aab", "aab")             # Expected: "aab"
    ]
    
    for s, t in test_cases:
        print(f"\nInput: s = \"{s}\", t = \"{t}\"")
        result = minWindow1(s, t)
        print(f"Output: \"{result}\"")
        print(f"Length: {len(result)}")
        
        # For the main example, show the window positions
        if s == "ADOBECODEBANC" and t == "ABC":
            print("\nVisualization of window movement:")
            print("1. First valid window: 'ADOBEC'")
            print("2. Shrinking from left...")
            print("3. Found smaller window: 'BECODEBA'")
            print("4. Shrinking from left...")
            print("5. Found smallest window: 'BANC'")
