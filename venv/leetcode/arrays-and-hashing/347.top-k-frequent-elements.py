from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count after loop: {1:3, 2:2, 3:1}
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # arr = [] creates a list to store pairs [count, number].
        arr = []

        # for num, cnt in count.items(): iterates over each key-value pair in count.
        # num = the number
        # cnt = frequency of that number
        # This is convenient because Python’s sort() sorts lists by the first element, then second, etc.
        for num, cnt in count.items():
            arr.append([cnt, num])

        # arr = [[3,1],[2,2],[1,3]]
        arr.sort()

        result = []
        while k > 0:
            result.append(arr.pop()[1])  # arr.pop()[1] takes the number part of that pair.
            k -= 1

        return result


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output [1,2]
