class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best_res = 0
        min_sum = float('inf')
        max_sum = float('-inf')

        for num in nums:
            max_sum = max(num,  max_sum + num)
            min_sum = min(num, min_sum + num)

            best_res = max(best_res, max_sum, abs(min_sum))

        return best_res
