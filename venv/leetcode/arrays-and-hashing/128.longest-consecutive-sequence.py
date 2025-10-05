def longestConsecutive(nums) -> int:
    # set automatically sorts the numbers in the array
    # numSet: {1, 2, 3, 4, 100, 200}
    numSet = set(nums)
    longest = 0
    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


print(longestConsecutive([99, 2, 1, 3, 5]))  # Output: 3
print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
print(longestConsecutive([1, 0, 1, 2]))  # Output: 3
