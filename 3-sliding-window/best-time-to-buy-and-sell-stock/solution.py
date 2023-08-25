from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day, sell_day = 0, 0
        profit = 0

        while sell_day < len(prices):
            print(prices[buy_day], prices[sell_day])
            profit = max(profit, prices[sell_day] - prices[buy_day])

            while buy_day < sell_day and prices[buy_day] > prices[sell_day]:
                buy_day += 1

            sell_day += 1

        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
