class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0] * (n + 1)

        # def rec(num):
        #     if dp[num] != 0:
        #         return dp[num]

        #     if num == 0:
        #         return 1

        #     multiply = 0
            
        #     for i in range(1, num + 1):
        #         multiply = max(multiply, rec(num - i) * i if i != n else 0)

        #     dp[num] = multiply
        #     return multiply

        # return rec(n)

        dp = [0] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]
