from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:

    res = []

    #sort input array
    nums.sort()

    #first loop to tell us the first value
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        #second loop to solve two sum using two pointers
        left = i + 1
        right = len(nums) - 1

        while left < right:
            threeSum = num + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-2,-2, 0, 0, 2, 2]))