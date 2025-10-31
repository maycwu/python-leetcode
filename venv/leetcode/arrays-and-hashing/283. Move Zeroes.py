"""
283. Move Zeroes (Easy)

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pass

# Test cases
test_cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([0, 0, 0, 1], [1, 0, 0, 0]),
    ([1, 0, 1], [1, 1, 0])
]

for nums, expected in test_cases:
    nums_copy = nums.copy()
    moveZeroes(nums_copy)
    print(f"Input: {nums}")
    print(f"Output: {nums_copy}")
    print(f"Expected: {expected}")
    print("✅" if nums_copy == expected else "❌")
    print()