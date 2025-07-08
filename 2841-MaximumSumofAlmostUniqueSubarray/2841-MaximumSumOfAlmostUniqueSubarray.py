from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        max_sum = 0
        n = len(nums)

        for i in range(n-k+1):
            sub_array = nums[i:k+i]

            if len(set(sub_array)) >= m:
                max_sum = max(max_sum, sum(sub_array))
        
        return max_sum
