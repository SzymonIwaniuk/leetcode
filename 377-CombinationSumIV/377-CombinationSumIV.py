class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Coin change
        # recursion 
        # memo = {}

        # def rec(i):
        #     if i in memo:
        #         return memo[i]

        #     if i == 0:
        #         return 1

        #     elif i < 0:
        #         return 0

        #     sub = 0

        #     for n in nums:
        #         sub += rec(i-n)

        #     memo[i] = sub
        #     return sub

        # return rec(target)
        
        # tabulation
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i-n]

        return dp[target]
