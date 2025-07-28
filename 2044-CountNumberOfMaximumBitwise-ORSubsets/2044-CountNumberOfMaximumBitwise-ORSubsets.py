class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bit = 0
        n = len(nums)

        for num in nums:
            max_bit |= num

        def rec(i, bit_or):
            if i == n:
                return 0
            
            cnt = 0

            if bit_or | nums[i] == max_bit:
                cnt = 2 ** (n - i) + rec(i + 1, bit_or)
            else:
                cnt = rec(i + 1, bit_or | nums[i]) + rec(i + 1, bit_or) + cnt

            return cnt
        
        return rec(0, 0) // 2

