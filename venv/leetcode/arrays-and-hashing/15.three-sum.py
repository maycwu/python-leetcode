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

    # use set to automatically avoid duplicate triplets
    results = set()

    # three pointers, i moves within the for loop, L and R pointers move within the while loop
    #[-4, -1, -1, 0, 1, 2]
    #  i   L            R

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            elif sum == 0:
                results.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
    # return [list(t) for t in results] #returns [[-1, 0, 1], [-1, -1, 2]]
    return list(results) #returns [(-1, 0, 1), (-1, -1, 2)]


print(threeSum(nums))  # [[-1,-1,2],[-1,0,1]]
print(threeSum(nums1))  # []
print(threeSum(nums2))  # [[0,0,0]]
print(threeSum(nums3))  # [[0,0,0]]
print(threeSum(nums4))  # [[-2,0,2],[-2,1,1]]

my_set = set()
my_set.add((1,2))
print([list(t) for t in my_set])


