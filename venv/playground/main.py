def find_min(a, b):
    """
    Returns the smaller of two values.
    
    Args:
        a: First value to compare
        b: Second value to compare
        
    Returns:
        The smaller of the two values
    """
    return a if a < b else b


def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: Length of the rectangle (positive number)
        width: Width of the rectangle (positive number)
        
    Returns:
        The area of the rectangle (length * width)
        
    Raises:
        ValueError: If either length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

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