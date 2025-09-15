class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        dp = [[float('inf') for _ in range(n)] for __ in range(n)]

        # def rec(i, j):
        #     if dp[i][j] != float('inf'):
        #         return dp[i][j]

        #     if j - i < 2:
        #         return 0

        #     mini = float('inf')

        #     for d in range(i+1, j):
        #         mini = min(
        #             mini, 
        #             rec(i,d) + rec(d,j) + values[i] * values[d] * values[j]
        #         )    

        #     dp[i][j] = mini
        #     return mini

        # ans = rec(0, n-1)
        # print(dp)
        # return ans

        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if j - i < 2:
                    dp[i][j] = 0
                else:
                    for d in range(i+1, j):
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i][d] + dp[d][j] + values[i] * values[d] * values[j]
                        )

        # print(dp)
        return dp[0][n-1]
