class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        sum_stones_from_left = [0] * (n+1)
        
        for i in range(n):
            sum_stones_from_left[i+1] = sum_stones_from_left[i] + stones[i]

        # dp = [[None for _ in range(n)] for __ in range(n)]
        # def rec(i, j):
        #     if dp[i][j] is not None:
        #         return dp[i][j]

        #     if i == j:
        #         return 0

        #     maxi = max(
        #         sum_stones_from_left[j+1] - sum_stones_from_left[i+1] - rec(i+1, j),
        #         sum_stones_from_left[j] - sum_stones_from_left[i] - rec(i, j-1)
        #     )

        #     dp[i][j] = maxi
        #     return maxi
        
        # ans = rec(0, n-1)
        # # print(dp)
        # return ans

        dp = [[0 for _ in range(n)] for __ in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = max(
                    dp[i][j],
                    sum_stones_from_left[j+1] - sum_stones_from_left[i+1] - dp[i+1][j],
                    sum_stones_from_left[j] - sum_stones_from_left[i] - dp[i][j-1]               
                    )
        
        return dp[0][n-1]
