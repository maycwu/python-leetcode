"""
136. Single Number (Easy)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.
"""

def singleNumber(nums: list[int]) -> int:
    pass

# Test cases
test_cases = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
    ([1, 1, 2, 2, 3], 3),
    ([-1, -1, -2], -2)
]

for nums, expected in test_cases:
    result = singleNumber(nums)
    print(f"nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("✅" if result == expected else "❌")
    print()