class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        res = 1
        cur = 1

        for i in range(1, n):
            if prices[i-1] - prices[i] == 1:
                cur += 1
            else:
                cur = 1
            res += cur 

        return res
