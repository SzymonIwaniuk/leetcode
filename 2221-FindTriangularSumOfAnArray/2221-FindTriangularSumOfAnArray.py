class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums

        for i in range(n-1):
            new_dp = []
            for j in range(n-i-1):
                new_dp.append((dp[j]+dp[j+1]) % 10)
            
            dp = new_dp

        return dp[0]
