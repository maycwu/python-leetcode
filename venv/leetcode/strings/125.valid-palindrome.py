def isPalindrome( s: str) -> bool:

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() == s[right].lower():
            right -= 1
            left += 1
        elif not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            return False
    return True


print(isPalindrome("Was it a car or a cat I saw?"))