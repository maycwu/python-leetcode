"""
977. Squares of a Sorted Array (Easy)

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""

def sortedSquares(nums: list[int]) -> list[int]:
    pass

# Test cases
test_cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([-5, -3, -2, -1], [1, 4, 9, 25]),
    ([0, 1, 2, 3], [0, 1, 4, 9]),
    ([-1], [1])
]

for nums, expected in test_cases:
    result = sortedSquares(nums)
    print(f"nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("✅" if result == expected else "❌")
    print()