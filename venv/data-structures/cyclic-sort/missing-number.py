# Statement
# Given an array, nums, containing n distinct numbers in the range [0,n],
# return the only number in the range that is missing from the array.
#
#
# What would be the output if the following array is given as input?
#
# [0, 2, 4, 6, 7, 8, 3, 9, 5, 10]
#
# Output: 1 (In the range [0,10], 1 is missing from the array.)

def find_missing_number(nums):
    len_nums = len(nums)
    index = 0

    while index < len_nums:
        value = nums[index]

        if value < len_nums and value != nums[value]:
            nums[index], nums[value] = nums[value], nums[index]

        else:
            index += 1

    for x in range(len_nums):
        if x != nums[x]:
            return x
    return len_nums

def main():
    inputnumbers = [[4, 0, 3, 1],
                    [8, 3, 5, 2, 4, 6, 0, 1],
                    [1, 2, 3, 4, 6, 7, 8, 9, 10, 5],
                    [0],
                    [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23]
                    ]
    i = 1
    for x in inputnumbers:
        print(i, ".\tnums: ", x, sep = "")
        print("\n\tMissing number: ", find_missing_number(x), sep = "")
        print("-"*100, "\n", sep = "")
        i+=1

if __name__ == "__main__":
    main()