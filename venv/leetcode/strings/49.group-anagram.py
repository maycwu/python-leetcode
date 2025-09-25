from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word)) # act
            anagrams[sorted_word].append(word)
        return list(anagrams.values())


sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))