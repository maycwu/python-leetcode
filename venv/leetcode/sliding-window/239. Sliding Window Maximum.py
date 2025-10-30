# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7


# Not optimized solution, O(n * n), could be more efficient
def maxSlidingWindow(nums, k):
    result = []

    for i in range(len(nums) - k + 1):
        window = nums[i:k + i]
        maxWindowValue = max(window)
        result.append(maxWindowValue)
    return result


print(maxSlidingWindow([1, -1], 1))  # Output: [1, -1]
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]

"""
Sliding Window Maximum - Visual Explanation

Problem: Given an array of integers and a window size k, find the maximum in each window of size k.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Visual Walkthrough:

Initial State:
- Array: [1, 3, -1, -3, 5, 3, 6, 7]
- Indices: 0  1   2   3  4  5  6  7
- Window size k = 3
- Deque: []  (stores indices of elements in the current window)
- Result: []

Step 1: i = 0, num = 1
- Window: [1
- Deque: [0]  (add index 0)
- Current max: 1

Step 2: i = 1, num = 3
- Remove indices with values <= 3 from deque (remove 0)
- Add index 1
- Window: [1, 3
- Deque: [1]  (value: 3)
- Current max: 3

Step 3: i = 2, num = -1
- Add index 2 (since -1 < 3, we keep both)
- Window: [1, 3, -1]  (first complete window)
- Deque: [1, 2]  (values: [3, -1])
- Result: [3]  (max of first window)
- Remove index 0 from deque (out of window)

Step 4: i = 3, num = -3
- Add index 3
- Window: [3, -1, -3]
- Deque: [1, 2, 3]  (values: [3, -1, -3])
- Result: [3, 3]
- Remove index 1 from deque (out of window)

Step 5: i = 4, num = 5
- Remove indices with values <= 5 (remove 2,3)
- Add index 4
- Window: [-1, -3, 5]
- Deque: [4]  (value: [5])
- Result: [3, 3, 5]

... (continuing through the array)

Final Result: [3, 3, 5, 5, 6, 7]

Key Insights:
1. The deque maintains indices of elements in the current window in decreasing order
2. The front of the deque always has the maximum for the current window
3. We remove elements from the back of deque that are smaller than current element
4. We remove elements from the front that are outside the current window
"""

from collections import deque


def maxSlidingWindow(nums, k):
    if not nums:
        return []

    result = []
    dq = deque()  # stores indices of elements in the window

    for i, num in enumerate(nums):
        # Remove elements not in the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()

        # Add current element's index
        dq.append(i)

        # The front of deque is the maximum for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test cases
test_cases = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),  # Expected: [3,3,5,5,6,7]
    ([1], 1),  # Expected: [1]
    ([1, -1], 1),  # Expected: [1, -1]
    ([9, 11], 2),  # Expected: [11]
    ([4, -2], 2),  # Expected: [4]
]

for nums, k in test_cases:
    print(f"\nInput: nums = {nums}, k = {k}")
    result = maxSlidingWindow(nums, k)
    print(f"Output: {result}")

    # Print visualization for the first test case
    if nums == [1, 3, -1, -3, 5, 3, 6, 7] and k == 3:
        print("\nDetailed Visualization:")
        dq = deque()
        for i, num in enumerate(nums):
            # Show current state
            print(f"\nStep {i}: num = {num}")
            print(f"Before - Deque: {[nums[idx] for idx in dq]}")

            # Remove elements not in the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # Add current element's index
            dq.append(i)

            # Show window and current max
            window = nums[max(0, i - k + 1):i + 1]
            current_max = nums[dq[0]] if dq else None
            print(f"After  - Deque: {[nums[idx] for idx in dq]}")
            print(f"Window: {window}, Current max: {current_max}")
