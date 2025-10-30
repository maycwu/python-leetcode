# Example 1:
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
# The only good substring of length 3 is "xyz"
# .
# Example 2:
# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

# Input: s = "xyzzaz"
def countGoodSubstrings(s):
    count = 0
    for i in range((len(s) - 3 + 1)):
        sub_string = s[i:3 + i]
        if len(set(sub_string)) == 3:
            count += 1
    return count


print(countGoodSubstrings("xyzzaz"))  # Output: 1
print(countGoodSubstrings("aababcabc"))  # Output: 4
