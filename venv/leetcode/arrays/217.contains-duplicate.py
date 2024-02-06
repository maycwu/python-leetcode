# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from typing import List

# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Edge cases
# Input: nums = [0]
# Output: true

# Approach: create a set to store unique elements

# nums = [1, 2, 3, 1]
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums = [2, 14, 18, 22, 22]


def contains_duplicate(nums):
    if len(nums) <= 1:
        return False

    unique_values = set()
    for n in nums:
        if n in unique_values:
            return True
        else:
            unique_values.add(n)
    return False


print(contains_duplicate(nums))

# Time - O(n)
# Space - O(1)
