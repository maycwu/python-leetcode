from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # buy pointer
        right = 1  # sell pointer
        max_profit = 0
        while right < len(prices):
            # is this profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit) # update max_profit if this profit is bigger
            else:
                left = right
            right += 1
        return max_profit


sol = Solution()
sol.maxProfit([7, 1, 5, 3, 6, 4])  # Output: 5
