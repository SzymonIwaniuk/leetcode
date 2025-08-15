class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=lJxuwClVN2w <-- good tutorial
        """
        n = len(prices)
        profit = [0] * n

        for i in range(k):
            pos = -prices[0]

            for j in range(1, n):
                pos = max(pos, profit[j] - prices[j])
                profit[j] = max(profit[j], profit[j-1], pos + prices[j])

        # print(profit)
        return profit[-1]
