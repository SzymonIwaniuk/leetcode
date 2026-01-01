class Solution:
    def minInsertions(self, s: str) -> int:
        # before processing i, j need calculate
        # i + 1, j - 1
        # i + 1 -> increases 
        # j - 1 -> decreases
        # since i >= j returns 0, we only need to calculate j from i + 1 to n
        # bounds
        # dp[i][i] = 0 for all i [0 -> n) 
        # cuz when i >= j, we return 0 and no further iteration is needed
        # edge cases
        # 1 <= s.length <= 500 there's no need to except for empty string 
        
        n = len(s)
        dp = [[0] * n for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i + 1][j] + 1,
                        dp[i][j - 1] + 1
                    )

        return dp[0][n - 1]

        # memo = {}
        # def rec(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if i >= j:
        #         return 0
            
        #     mini = float("inf")

        #     if s[i] == s[j]:
        #         mini = min(mini, rec(i + 1, j - 1))

        #     else:
        #         mini = min(
        #             mini, 
        #             rec(i + 1, j) + 1, 
        #             rec(i, j - 1) + 1
        #             )
            
        #     memo[(i, j)] = mini
        #     return mini
        
        # return rec(0, len(s) - 1)
