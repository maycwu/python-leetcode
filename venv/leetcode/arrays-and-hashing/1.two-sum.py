# Find the index of two numbers that add to the target number

array = [6, 2, 0, 4]
target = 10


def two_sum(array, target):
    matches = {}
    for i in range(len(array)):
        match = target - array[i]
        if match in matches:
            return [i, matches[match]]
        else:
            matches[array[i]] = i


print(two_sum(array, target))
