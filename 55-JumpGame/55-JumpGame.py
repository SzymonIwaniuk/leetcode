class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_idx = 0

        for i in range(n):
            if i <= max_idx:
                max_idx = max(max_idx, i + nums[i])
            else:
                return False
                
        return max_idx >= n - 1
