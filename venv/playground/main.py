def lengthOfLongestSubstring(s):
    #  seen = {
    #     a : 3,
    #     b : 4,
    #     c : 2,
    #  }
    #  s = "abcabcbb"
    #        l r

    seen = {}
    longest = 0
    left = 0
    right = 0

    for right in range(len(s)):
        if s[right] in seen:
            # move the left pointer to the letter that was seen before
            # "max" ensures the window doesn't go backwards i.e "abba"
            left = max(left,seen[s[right]] + 1)

        # update current character to seen map
        seen[s[right]] = right

        # calculate window size
        current_length = right - left + 1
        longest = max(longest, current_length)

    return longest


print(lengthOfLongestSubstring("pwwkew"))  # Output = 3
