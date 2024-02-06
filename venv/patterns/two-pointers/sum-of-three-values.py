# Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target,
# that is, nums[i] + nums[j] + nums[k] == target.
# Return TRUE if three such integers exist in the array. Otherwise, return FALSE

# SOLUTION
# 1) Sort the input array in ascending order (low to high)
# 2) Iterate over the entire sorted array to find the triplet whose sum is equal to the target
# 3) In each iteration, make a triplet by storing the current array element and the other two elements using two pointers (low and high), and calculate their sum
# 4) Adjust the calculated sum value, until it becomes equal to the target value, by conditionally moving the pointers low and high
# 5) Return TRUE if the required sum is found. Otherwise, return FALSE

# Inputs
nums = [-1, 2, 1, 4, -2]  # TRUE
target = 1

nums1 = [3, 7, 1, 2, 8, 4, 5]  # TRUE
target1 = 10

nums2 = [3, 7, 1, 2, 8, 4, 5]  # FALSE
target2 = 21

nums3 = [-1, 2, 1, -4, 5, -3]  # TRUE
target3 = -8

nums4 = [-1, 2, 1, -4, 5, -3]  # TRUE
target4 = 0


def find_sum_of_three(nums, target):
    nums.sort()

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while (left < right):
            sum = nums[i] + nums[left] + nums[right]
            if sum == target:
                return True
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
    return False


print(find_sum_of_three(nums, target))
print(find_sum_of_three(nums1, target1))
print(find_sum_of_three(nums2, target2))
print(find_sum_of_three(nums3, target3))
print(find_sum_of_three(nums4, target4))
