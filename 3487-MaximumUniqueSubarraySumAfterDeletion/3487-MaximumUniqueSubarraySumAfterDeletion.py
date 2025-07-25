class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        unique = set()
        maxi = -1000
        res = 0

        for i in range(n):
            num = nums[i]

            if num not in unique and num >= 0:
                unique.add(num)
                res += num

            maxi = max(maxi, num)
        
        return res if res != 0 else maxi
