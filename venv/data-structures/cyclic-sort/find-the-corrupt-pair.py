# Statement
# We are given an unsorted array, nums, with n elements and each element is in the range [1,n]
# inclusive. The array originally contained all the elements from 1 to n
# but due to a data error, one of the numbers is duplicated, which causes another number missing.
# Find and return the corrupt pair (missing, duplicated).
#
# Which is the corrupt pair in the array given below?
#
# [4, 1, 3, 4, 5]
#
# Ouput: 2, 4 (The missing number is 2, and the duplicate number is 4.)
#
# [6, 1, 2, 4, 5, 5]
# Output: 3, 5 (The missing number is 3, and the duplicate number is 5.)
#
# [8, 1, 2, 3, 4, 3, 6, 7]
# Output: 3,5 (The missing number is 5, and the duplicate number is 3.)

def find_corrupt_pair(nums):
    # Initialize missing and duplicated
    missing = None
    duplicated = None

    # Function for swapping
    def swap(arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]
    # Apply cyclic sort on the array

    i = 0
    # Traversing the whole array
    while i < len(nums):
        # Determining what position the specific element should be at
        correct = nums[i] - 1
        # Check if the number is at wrong position
        if nums[i] != nums[correct]:
            # Swapping the number to it's correct position
            swap(nums, i, correct)
        else:
            i += 1

    # Finding the corrupt pair(missing, duplicated)

    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicated = nums[j]
            missing = j + 1
    return [missing, duplicated]

# Driver code

def main():
    array = [[3, 1, 2, 5, 2],
             [3, 1, 2, 3, 6, 4],
             [4, 1, 2, 1, 6, 3],
             [4, 3, 4, 5, 1],
             [5, 3, 5, 6, 2, 1]]
    for i in range(len(array)):
        print(i + 1,  ".\tGiven array: ", array[i], sep="")
        result = find_corrupt_pair(array[i])
        print("\n\tCorrupt pair: ", result[0], ", ", result[1], sep="")
        print("-"*100)


if __name__ == '__main__':
    main()
