class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        heights = [nums[0]]

        # Unique
        for p in range(1, n):
            if nums[p] is not heights[-1]:
                heights.append(nums[p])

        m = len(heights)
        cnt = 0
        
        # Count vallies and hills 
        for p in range(1, m - 1):
            height = heights[p]

            if heights[p - 1] < height and heights[p + 1] < height:
                cnt += 1

            elif heights[p - 1] > height and heights[p + 1] > height:
                cnt += 1

        return cnt
