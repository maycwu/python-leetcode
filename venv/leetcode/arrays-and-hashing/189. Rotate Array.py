"""
189. Rotate Array (Medium)

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5
"""

def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pass

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([1, 2], 3, [2, 1]),
    ([1], 0, [1]),
    ([1, 2, 3], 4, [3, 1, 2])
]

for nums, k, expected in test_cases:
    nums_copy = nums.copy()
    rotate(nums_copy, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {nums_copy}")
    print(f"Expected: {expected}")
    print("✅" if nums_copy == expected else "❌")
    print()