"""
448. Find All Numbers Disappeared in an Array (Easy)

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n
"""

def findDisappearedNumbers(nums: list[int]) -> list[int]:
    pass

# Test cases
test_cases = [
    ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
    ([1, 1], [2]),
    ([1, 2, 3], []),
    ([], []),
    ([2, 2], [1])
]

for nums, expected in test_cases:
    result = findDisappearedNumbers(nums)
    print(f"nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("✅" if result == expected else "❌")
    print()