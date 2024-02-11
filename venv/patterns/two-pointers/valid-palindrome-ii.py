# Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

str = "DEEAD"  # TRUE
str1 = "abca"  # TRUE


def validPalindrome(str):
    left = 0
    right = len(str) - 1
    counter = 0

    while left < right:
        if str[left] != str[right]:
            skipLeft = checkPalindrome(left + 1, right, str)
            skipRight = checkPalindrome(left, right - 1, str)
            return skipLeft or skipRight
        else:
            left += 1
            right -= 1
    return True


def checkPalindrome(left, right, str):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(validPalindrome("aaaax"))
print(validPalindrome("aba"))
