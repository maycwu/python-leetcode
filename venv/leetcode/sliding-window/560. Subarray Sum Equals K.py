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


print(subarraySum([1, 1, 1], 2))  # Output: 2
print(subarraySum([1, 2, 3], 3))  # Output: 2
print(subarraySum([2, -1, 3, -2], 2))  # Output: 3
print(subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4
print(subarraySum([2, -1, -3, 4, 2, 3], 5))  # Output: 2