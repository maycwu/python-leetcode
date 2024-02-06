# https://leetcode.com/problems/valid-palindrome/

# 1) Initialize two pointers at the beginning and end of the string
# 2) Create a character bank for only valid characters we can traverse through.
# 3) Check whether the current pair of characters is identical. If identical, move both pointers by one index toward the middle
# 4) If the character is NOT in the bank, move the pointer by 1 index
# 5) If they are not identical, return FALSE.
# 6) Keep traversing them toward the middle until they meet.
# 7) If we reach the middle of the string without finding a mismatch, return TRUE

str = "A man, a plan, a canal: Panama"
str1 = 'hello'
str2 = 'RACEACAR'
str3 = "A"
str4 = "ABCDABCD"
str5 = 'baab'


def valid_palindrome(s):
    char_bank = "abcdefghijkmnlopqrstuvwyzx0123456789"
    s = s.lower()
    s = s.split(" ")
    s = ''.join(s)

    if len(s) < 1:
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] not in (char_bank):
            left += 1
        elif s[right] not in (char_bank):
            right -= 1
        else:
            return False
    return True


print(valid_palindrome(str))  # true
print(valid_palindrome(str1))  # false
print(valid_palindrome(str2))  # false
print(valid_palindrome(str3))  # true
print(valid_palindrome(str4))  # false
print(valid_palindrome(str5))  # true
