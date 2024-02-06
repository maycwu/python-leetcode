# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Inputs
nums = [-1, 0, 1, 2, -1, -4]
nums1 = [0, 1, 1]
nums2 = [0, 0, 0]
nums3 = [0, 0, 0, 0]
nums4 = [-2, 0, 1, 1, 2]


def threeSum(nums):
    nums.sort()
    results = set()

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while (left < right):
            sum = nums[i] + nums[left] + nums[right]
            # if equal to zero, add to results set and move the pointers by 1 index
            if sum == 0:
                results.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
    return list(results)


print(threeSum(nums))  # [[-1,-1,2],[-1,0,1]]
print(threeSum(nums1))  # []
print(threeSum(nums2))  # [[0,0,0]]
print(threeSum(nums3))  # [[0,0,0]]
print(threeSum(nums4))  # [[-2,0,2],[-2,1,1]]
