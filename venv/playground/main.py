def threeSum(nums):
    # Input: nums = [-1,0,1,2,-1,-4]
    # Sorted = [-4,-1,-1,0,1,2]
    # Output: [[]]

    nums.sort()

    result = set()

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        current = nums[i]

        if nums[i] == nums[i] - 1:
            continue
        while left < right:
            numSum = current + nums[left] + nums[right]
            if numSum == 0:
                result.add((current, nums[left], nums[right]))
                left += 1
                right -= 1
            elif numSum > 0:
                right -= 1
            elif numSum < 0:
                left += 1
    return [list(t) for t in result]

print(threeSum([-1,0,1,2,-1,-4]))