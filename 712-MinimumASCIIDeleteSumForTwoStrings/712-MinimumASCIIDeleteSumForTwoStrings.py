class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        # prefix_s1 = [0] * (n + 1)
        # prefix_s2 = [0] * (m + 1)
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 0

        # BOTTOM UP
        # 1 base cases
        #     if i == n:
        #         return prefix_s2[j]

        #     elif j == m:
        #         return prefix_s1[i]  

        for i in range(n - 1, -1, -1):
            # prefix_s1[i] = ord(s1[i]) + prefix_s1[i + 1]
            # dp[i][m] = prefix_s1[i]
            dp[i][m] = ord(s1[i]) + dp[i + 1][m]
        
        for j in range(m - 1, -1, -1):
            # prefix_s2[j] = ord(s2[j]) + prefix_s2[j + 1]
            # dp[n][j] = prefix_s2[j]
            dp[n][j] = ord(s2[j]) + dp[n][j + 1]

        # 2 process f(i + 1, j + 1), f(i + 1, j), f(i, j + 1) before f(i , j)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        dp[i + 1][j] + ord(s1[i]),
                        dp[i][j + 1] + ord(s2[j]),
                    )
        
        # 3 return result f(0, 0)
        return dp[0][0]

        # TOP DOWN
        # def rec(i, j):
        #     if i == n:
        #         return prefix_s2[j]

        #     elif j == m:
        #         return prefix_s1[i]    
            
        #     if dp[i][j] != float("inf"):
        #         return dp[i][j]

        #     if s1[i] == s2[j]:
        #         mini = rec(i + 1, j + 1)

        #     else:
        #         mini = min(
        #             rec(i + 1, j) + ord(s1[i]),
        #             rec(i, j + 1) + ord(s2[j]),
        #         )

        #     dp[i][j] = mini
        #     return mini

        # return rec(0, 0)
