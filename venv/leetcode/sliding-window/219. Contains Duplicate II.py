# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# This approach efficiently checks for duplicates within
# the specified range using a sliding window and a set for quick lookups.
def containsNearbyDuplicate(nums, k):
    # Use a set to store elements in the current window
    window = set()

    for i in range(len(nums)):
        # If current element is in the window, we found a duplicate within distance k
        if nums[i] in window:
            return True

        # Add current element to the window
        window.add(nums[i])

        # If window size exceeds k, remove the leftmost element
        if len(window) > k:
            window.remove(nums[i - k])

    return False


nums = [1, 2, 3, 4, 1]
print(nums[-4])

# print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
# print(containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False
