class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m = len(b)
        inf = float('-inf')
        dp = [[inf] * (m + 1) for _ in range(5)]
        
        for i in range(m + 1):
            dp[0][i] = 0

            
        # top down
        # def rec(i, j):
        #     if i == 4:
        #         return 0
            
        #     if i < 4 and j > m - 1:
        #         return inf
            
        #     if dp[i][j] != inf:
        #         return dp[i][j]

        #     maxi = max(
        #         a[i] * b[j] + rec(i + 1, j + 1),
        #         rec(i, j + 1)
        #     )

        #     dp[i][j] = maxi
        #     return maxi

        # return rec(0, 0)


        for i in range(1, 5):
            for j in range(1, m + 1):
                dp[i][j] = max(
                    dp[i-1][j-1] + a[i-1] * b[j-1],
                    dp[i][j-1]
                    )
        
        return max(dp[4])
