# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average
# value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#
# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000


def findMaxAverage(nums, k):
    # nums = [1,12,-5,-6,50,3], k = 4
    # get window_size based on k

    # Edge case: if k equals array length, return average of entire array
    if len(nums) == k:
        return sum(nums) / k

    # Calculate the sum of first window
    window_sum = sum(nums[:k])
    max_average = window_sum / k

    left = 0
    # slide the window through the array
    for right in range(k, len(nums)):
        # Update window sum by removing leftmost element
        window_sum -= nums[left]
        left += 1

        # Adding new right element
        window_sum += nums[right]

        max_average = max(window_sum / k, max_average)

    return max_average


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
print(findMaxAverage([4, 0, 4, 3, 3], 5))
