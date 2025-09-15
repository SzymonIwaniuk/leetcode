class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix_sums = [0] * (n + 1)
        
        for i in range(n):
            prefix_sums[i+1] = stones[i] + prefix_sums[i]

        dp = [[float('inf') for _ in range(n)] for __ in range(n)]

        # def rec(i, j):
        #     if dp[i][j] != float('inf'):
        #         return dp[i][j]

        #     if i == j:
        #         dp[i][j] = 0
        #         return 0

        #     mini = float('inf')

        #     for d in range(i, j, k-1):
        #         mini = min(
        #             mini,
        #             rec(i, d) + rec(d+1,j)
        #         )

        #     if (j - i) % (k - 1) == 0:
        #         mini += prefix_sums[j + 1] - prefix_sums[i]

        #     dp[i][j] = mini
        #     return mini

        # return rec(0, n-1)
        
        for i in range(n):
            dp[i][i] = 0

        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                for d in range(i, j, k-1):
                    dp[i][j] = min(dp[i][j], dp[i][d] + dp[d+1][j])

                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix_sums[j + 1] - prefix_sums[i]                    
                    
        return dp[0][n-1]
