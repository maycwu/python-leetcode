def maxArea(height):
    # area = l * w
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
# print(maxArea([1, 7, 2, 5, 4, 7, 3, 6]))  # Output: 36
# print(maxArea([2, 2, 2]))  # Output: 4
print(maxArea([8, 7, 2, 1]))  # Output: 7
