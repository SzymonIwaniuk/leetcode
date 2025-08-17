class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for i in range(n)]
        parents = [[None] * n for i in range(n)]

        def rec(i, j):
            dp[i][j] += grid[i][j]

            if i + 1 < n and grid[i + 1][j] != -1 and dp[i + 1][j] <= dp[i][j]:
                parents[i + 1][j] = (i, j)
                dp[i + 1][j] = dp[i][j]
                rec(i + 1, j)

            if j + 1 < n and grid[i][j + 1] != -1 and dp[i][j + 1] <= dp[i][j]:
                parents[i][j + 1] = (i, j)
                dp[i][j + 1] = dp[i][j]
                rec(i, j + 1)

        rec(0, 0)
        i, j = n-1, n-1
        path = set([(i, j)])

        while parents[i][j] != None:
            path.add(parents[i][j])
            i, j = parents[i][j][0], parents[i][j][1]

        back_dp = [[0] * n for i in range(n)]
        def back(i ,j):
            if grid[i][j] == 1 and (i, j) not in path:
                back_dp[i][j] += 1

            if i - 1 >= 0 and grid[i - 1][j] != -1 and back_dp[i - 1][j] <= back_dp[i][j]:
                back_dp[i - 1][j] = back_dp[i][j]
                back(i - 1, j)

            if j - 1 >= 0 and grid[i][j - 1] != -1 and back_dp[i][j - 1] <= back_dp[i][j]:
                back_dp[i][j - 1] = back_dp[i][j]
                back(i, j - 1)

        back(n-1, n-1)

        return dp[n-1][n-1] + back_dp[0][0]
