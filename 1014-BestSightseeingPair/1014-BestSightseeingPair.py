class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = cur = 0

        for val in values:
            res = max(res, cur + val)
            cur = max(cur, val) - 1
        
        return res
