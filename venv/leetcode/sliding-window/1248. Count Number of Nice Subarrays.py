# TODO: Implement this function

# Given an array of integers nums and an integer k.
# A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
#
# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
#
# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

def numberOfSubarrays(nums, k):
    """
    Count the number of subarrays with exactly k odd numbers.

    Approach:
    1. Convert the problem to a prefix sum problem where we track the count of odd numbers.
    2. Use a hash map to store the frequency of prefix sums.
    3. For each number, if it's odd, increment the current count.
    4. Check if (current_count - k) exists in the hash map and add its frequency to the result.

    Visual Example:
    nums = [1,1,2,1,1], k = 3

    Index | num | odd? | curr_count | curr_count - k | prefix_counts           | Subarrays Found
    ------|-----|------|------------|----------------|-------------------------|----------------
    -     | -   | -    | 0          | -3             | {0:1}                   | -
    0     | 1   | Yes  | 1          | -2             | {0:1, 1:1}              | -
    1     | 1   | Yes  | 2          | -1             | {0:1, 1:1, 2:1}          | -
    2     | 2   | No   | 2          | -1             | {0:1, 1:1, 2:2}          | -
    3     | 1   | Yes  | 3          | 0              | {0:1, 1:1, 2:2, 3:1}     | [1,1,2,1]
    4     | 1   | Yes  | 4          | 1              | {0:1, 1:1, 2:2, 3:1, 4:1}| [1,2,1,1], [2,1,1], [1,1]

    Final Answer: 2
    """
    from collections import defaultdict

    # Initialize prefix_counts with {0:1} to handle the case when the first k elements form a nice subarray
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    curr_count = 0
    result = 0

    for num in nums:
        # Increment curr_count if the current number is odd
        if num % 2 == 1:
            curr_count += 1

        # If (curr_count - k) exists in prefix_counts, add its frequency to result
        result += prefix_counts.get(curr_count - k, 0)

        # Update the prefix_counts with current count
        prefix_counts[curr_count] += 1

    return result


# Test Cases
test_cases = [
    ([1, 1, 2, 1, 1], 3),  # Output: 2
    ([2, 4, 6], 1),  # Output: 0 (no odd numbers)
    ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2),  # Output: 16
    ([1, 1, 1, 1, 1], 1),  # Output: 5
    ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)  # Output: 3
]

for nums, k in test_cases:
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Number of nice subarrays: {numberOfSubarrays(nums, k)}\n")

