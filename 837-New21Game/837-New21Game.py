class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # memo = {}

        # def rec(p):
        #     if p in memo:
        #         return memo[p]

        #     if p >= k:
        #         if p <= n:
        #             return 1
        #         return 0

        #     sub = 0

        #     for i in range(1, maxPts + 1):
        #         sub += rec(p + i) / maxPts

        #     memo[p] = sub
        #     return sub

        # proability = rec(0)
        # return proability
        
        if k == 0 or n >= k + maxPts - 1:
            return 1.0 

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return sum(dp[k:])

