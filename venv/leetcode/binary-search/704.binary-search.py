from typing import List


# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
#
# Example 1:
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3


# Example 2:
# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # With  while left <= right: The loop runs and finds the target.
        # With while left < right: The loop doesn't run, and we miss the target.
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] > target:
                right = middle - 1
            if nums[middle] == target:
                return middle
        return -1


solution = Solution()
print(solution.search([-1, 0, 2, 4, 6, 8], 4))  # Output: 3
print(solution.search([-1, 0, 2, 4, 6, 8], 3))  # Output: -1
print(solution.search([0, 1, 2, 3, 4, 5, 6], 4))  # Output: 4
