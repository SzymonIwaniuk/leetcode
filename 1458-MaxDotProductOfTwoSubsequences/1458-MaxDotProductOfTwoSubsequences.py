class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[[float("-inf"), float("-inf")] for _ in range(m + 1)] for __ in range(n + 1)]
        # base cases
        for i in range(n+1):
            dp[i][m][1] = 0

        for j in range(m+1):
            dp[n][j][1] = 0

        # before i compute (i, j, flag) i need to compute
        # (i + 1, j, f), (i, j + 1, f), (i + 1, j + 1, 1)
        # so iterate backwards 

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                for f in range(2):
                    dp[i][j][f] = max(
                        dp[i+1][j][f],
                        dp[i][j+1][f],
                        dp[i+1][j+1][1] + nums1[i] * nums2[j],
                    )

        return dp[0][0][0]

        # def rec(i, j, flag):
        #     if i == n or j == m:
        #         if flag:
        #             return 0
        #         return float("-inf")

        #     if dp[i][j][flag] != None:
        #         return dp[i][j][flag]

        #     # skip i
        #     # skip j
        #     # take i j
        #     maxi = max(
        #         rec(i + 1, j, flag),
        #         rec(i, j + 1, flag),
        #         rec(i + 1, j + 1, 1) + nums1[i] * nums2[j],
        #     )

        #     dp[i][j][flag] = maxi
        #     return maxi

        # return rec(0, 0, 0)
