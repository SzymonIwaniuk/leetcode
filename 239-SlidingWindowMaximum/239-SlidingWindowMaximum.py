import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []

        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        res = []

        for i in range(k-1, n):
            heapq.heappush(heap, (-nums[i], i))

            while heap:
                num, idx = heapq.heappop(heap)
                if idx >= i - k + 1:
                    res.append(-num)
                    heapq.heappush(heap, (num, idx))
                    break
        return res           

