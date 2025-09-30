# Given a string s, return the longest palindromic
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

def longestPalindrome(s):
    result = ''

    # helper function
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # After the loop exits, left and right are out of bounds or pointing to characters that do not match.
        # To get the valid palindrome substring, we need to adjust the indices:
        # left + 1: Moves left back to the last valid index where the characters matched.
        # right: Remains as the exclusive end index for slicing.
        return s[left + 1 : right]



    for i in range(len(s)):
        # Odd-length palindrome (center is a single character)
        odd_palindrome = expand_around_center(i, i)
        # Even-length palindrome (center is between two characters)
        even_palindrome = expand_around_center(i, i + 1)

        # Update the result if a longer palindrome is found,
        # key is a function that tells Python how to compare the elements when finding the maximum
        # since we want the longest string, we use key=len.
        # So Python checks len(result), len(odd_palindrome), and len(even_palindrome), and returns the string with the greatest length.
        result = max(result, odd_palindrome, even_palindrome, key=len)

    return result



word = "mayonaise"
print(word[1: 1])
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
