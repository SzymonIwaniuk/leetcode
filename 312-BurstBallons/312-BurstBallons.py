class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # interval dp 
        # dp[i][j] -> best from i to j index
    
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for __ in range(n)]
        
        # def rec(i, j):
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if i > j:
        #         return 0

        #     maxi = -1
        #     for k in range(i, j+1):
        #         maxi = max(
        #             maxi,
        #             rec(i, k-1) + nums[i-1] * nums[k] * nums[j+1] + rec(k+1, j)
        #         )
            
        #     dp[i][j] = maxi
        #     return maxi

        # return rec(1, n-2)


        for l in range(1, n-1):
            for i in range(1, n-l):
                j = i + l - 1
                for k in range(i, j+1):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k-1] + nums[i-1] * nums[k] * nums[j+1] + dp[k+1][j]
                    )

        print(dp)
        return dp[1][n-2]
