from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cheapest = prices[0]

        for p in prices[1: ]:
            if cheapest > p:
                cheapest = p
            maxProfit = max(maxProfit, p - cheapest)
            
        return maxProfit
            
solution = Solution()
res = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(res)