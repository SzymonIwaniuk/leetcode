from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        # Brute O(n^2)
        n = len(nums)
        res = 0

        for i in range(n):
            mpp = {}
            pairs = 0

            for j in range(i, n):
                pairs += mpp.get(nums[j], 0)
                mpp[nums[j]] = mpp.get(nums[j], 0) + 1

                if pairs >= k:
                    res += 1

        return res
