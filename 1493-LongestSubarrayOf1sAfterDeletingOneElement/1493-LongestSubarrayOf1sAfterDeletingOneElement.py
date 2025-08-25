class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = curr = 0
        tab = []

        for i in range(n):
            if nums[i] == 1:
                curr += 1
            else:
                tab.append(curr)
                curr = 0
        
        tab.append(curr)
        m = len(tab)
        
        if m == 1 and tab[0] > 0:
            return tab[0] - 1
            
        for j in range(m - 1):
            res = max(res, tab[j] + tab[j+1])

        return res
