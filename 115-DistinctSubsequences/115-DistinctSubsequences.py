class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if s[0] == t[0] else 0

        for i in range(1, n):
            if s[i] == t[0]:
                dp[0][i] = dp[0][i-1] + 1
            else:
                dp[0][i] = dp[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                if s[j] == t[i]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]


        return dp[m-1][n-1]
