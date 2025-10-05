# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2],
# such that they add up to a given target number target and index1 < index2.
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.
# Your solution must use O(1) additional space.

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:  # Continue until pointers meet
        if (numbers[left] + numbers[right]) == target:  # If sum matches target
            return [left + 1, right + 1]
        if (numbers[left] + numbers[right]) > target:  # If sum is too large
            right -= 1  # Move right pointer left to reduce sum
        else:  # If sum is too small
            left += 1  # Move left pointer right to increase sum


print(twoSum([1, 2, 3, 4], 4))  # [1, 3]
print(twoSum([2, 7, 11, 15], 9))  # [1,2]
print(twoSum([2, 3, 4], 6))  # [1,3]
