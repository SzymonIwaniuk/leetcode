class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for b in nums:
            if b == 0:
                if res % 2 == 1:
                    continue
                else:
                    res += 1

            else:
                if res % 2 == 0:
                    continue
                else:
                    res += 1

        return res
