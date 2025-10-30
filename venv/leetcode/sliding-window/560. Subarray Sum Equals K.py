# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2


# Brute force
# def subarraySum(nums, k):
#     count = 0
#     n = len(nums)
#
#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += nums[j]  # Add the current element to the running sum
#             if current_sum == k:    # Check if the sum equals k
#                 count += 1
#
#     return count

"""
Subarray Sum Equals K - Prefix Sum Visualization

Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7

Visualization of the prefix sum approach:

| Index | num | sum_arr | sum_arr - k | Check sum_arr - k in prefix_counts | Update prefix_counts                          | Subarrays Found |
|-------|-----|---------|-------------|-----------------------------------|----------------------------------------------- |-----------------|
| -     | -   | 0       | -7          | No (0 not in prefix_counts)       | {0:1}                                          | -               |
| 0     | 3   | 3       | -4          | No (-4 not in prefix_counts)      | {0:1, 3:1}                                     | -               |
| 1     | 4   | 7       | 0           | Yes (0 is in prefix_counts)       | {0:1, 3:1, 7:1}                                | [3,4]           |
| 2     | 7   | 14      | 7           | Yes (7 is in prefix_counts)       | {0:1, 3:1, 7:1, 14:1}                          | [7]             |
| 3     | 2   | 16      | 9           | No (9 not in prefix_counts)       | {0:1, 3:1, 7:1, 14:1, 16:1}                    | -               |
| 4     | -3  | 13      | 6           | No (6 not in prefix_counts)       | {0:1, 3:1, 7:1, 14:1, 16:1, 13:1}              | -               |
| 5     | 1   | 14      | 7           | Yes (7 is in prefix_counts)       | {0:1, 3:1, 7:1, 14:2, 16:1, 13:1}              | [7,2,-3,1]      |
| 6     | 4   | 18      | 11          | No (11 not in prefix_counts)      | {0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1}        | -               |
| 7     | 2   | 20      | 13          | Yes (13 is in prefix_counts)      | {0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1, 20:1}  | [1,4,2]          |

Key Observations:
1. We find a subarray when (sum_arr - k) exists in prefix_counts
2. The subarray is found between the index where (sum_arr - k) was first seen and current index
3. Total subarrays found: 4 ([3,4], [7], [7,2,-3,1], [1,4,2])
"""


# Prefix sum approach
def subarraySum(nums, k):
    count = 0
    sum_arr = 0
    prefix_counts = {0: 1}

    for num in nums:
        sum_arr += num
        if sum_arr - k in prefix_counts:
            count += prefix_counts[sum_arr - k]

        # update the seen prefix sum counts
        prefix_counts[sum_arr] = prefix_counts.get(sum_arr, 0) + 1

    return count

# Test cases
test_cases = [
    ([1, 1, 1], 2),          # Output: 2
    ([1, 2, 3], 3),          # Output: 2
    ([2, -1, 3, -2], 2),     # Output: 3
    ([3, 4, 7, 2, -3, 1, 4, 2], 7)  # Output: 4
]

for nums, k in test_cases:
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {subarraySum(nums, k)}")

# Prefix sum approach with defaultdict
# def subarraySum(nums, k):
#     count = 0
#     prefix_sums = defaultdict(int)
#     prefix_sums[0] = 1  # Base case: empty subarray has sum 0
#     current_sum = 0
#
#     for num in nums:
#         current_sum += num
#         # If (current_sum - k) exists in prefix_sums, we found subarrays that sum to k
#         count += prefix_sums.get(current_sum - k, 0)
#         # Add current sum to prefix_sums
#         prefix_sums[current_sum] += 1
#
#     return count


# Same logic as above but returns the sub-arrays instead of counts
# def subarraySum(nums, k):
#     prefix_sums = {0: [-1]}  # Maps prefix sum to list of indices where it occurs
#     current_sum = 0
#     result = []
#
#     for i, num in enumerate(nums):
#         current_sum += num
#
#         # Check if (current_sum - k) exists in prefix_sums
#         if (current_sum - k) in prefix_sums:
#             # Add all subarrays ending at current index
#             for start in prefix_sums[current_sum - k]:
#                 result.append(nums[start + 1:i + 1])
#
#         # Update the prefix_sums map
#         if current_sum not in prefix_sums:
#             prefix_sums[current_sum] = []
#         prefix_sums[current_sum].append(i)
#     return result

# print(subarraySum([1, 1, 1], 2))  # Output: 2
# print(subarraySum([1, 2, 3], 3))  # Output: 2
# print(subarraySum([2, -1, 3, -2], 2))  # Output: 3
# print(subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4
# print(subarraySum([2, -1, -3, 4, 2, 3], 5))  # Output: 2