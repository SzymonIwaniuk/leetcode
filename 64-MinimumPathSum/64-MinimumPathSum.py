class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        inf = float('inf')
        dp = [[inf] * m for i in range(n)]

        """Recursion with memoization"""
        # dp[0][0] = grid[0][0]

        # def rec(i, j):
        #     if i + 1 < n and dp[i][j] + grid[i + 1][j] < dp[i + 1][j]:
        #         dp[i + 1][j] = dp[i][j] + grid[i + 1][j]
        #         rec(i + 1, j)

        #     if j + 1 < m and dp[i][j] + grid[i][j + 1] < dp[i][j + 1]:
        #         dp[i][j + 1] = dp[i][j] + grid[i][j + 1]
        #         rec(i, j + 1)

        # rec(0, 0)
        # print(dp)
        # return dp[n-1][m-1]

        """Tabulation approach"""
        dp[0][0] = grid[0][0]
        
        # Base cases
        # for most left column 
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # for top row
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[n-1][m-1]

