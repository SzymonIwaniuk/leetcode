class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # n = len(nums)
        # nums.sort(reverse=True)
        # prefixsum = score = 0

        # for i in range(n):
        #     prefixsum += nums[i]
        #     if prefixsum > 0:
        #         score += 1

        #     else:
        #         return score
        # return score

        s, n = sum(nums), len(nums)
        heapq.heapify(nums)
        # print(nums)
        drops = 0
        while s <= 0 and nums:
            s -= heapq.heappop(nums)
            drops += 1
            # print(s)
            # print(drops)
        return n - drops  
        
