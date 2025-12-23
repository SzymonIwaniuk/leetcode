class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # n = len(nums)
        # suffix = [0] * n
        # multi = maxi = 0


        # for i in range(n - 1, -1, -1):
        #     multi = max(multi, nums[i])
        #     suffix[i] = multi
        
        # for i in range(n-2):
        #     j = i + 1
        #     while j < n - 1:
        #         maxi = max(maxi, (nums[i] - nums[j]) * suffix[j+1])
        #         j += 1

        # return maxi

        n = len(nums)
        suffix = [0] * n
        prefix = [0] * n
        max_k = max_i = maxi = 0

        for i in range(n):
            max_i = max(max_i, nums[i])
            prefix[i] = max_i

        for k in range(n - 1, -1, -1):
            max_k = max(max_k, nums[k])
            suffix[k] = max_k

        for j in range(1, n-1):
            maxi = max(maxi, (prefix[j-1] - nums[j]) * suffix[j+1])

        return maxi
