import heapq


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3

        mini = min(nums[:k])
        maxi = max(nums[2*k:])

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        max_heap = nums[2*k:]
        heapq._heapify_max(max_heap)

        dp_min = [float('inf')] * n
        dp_max = [float('-inf')] * n
        dp_min[k-1] = mini
        dp_max[2*k] = maxi

        print(dp_max, dp_min)
        for i in range(n // 3, n):
            if nums[i] <= mini:
                num = heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
                mini = nums[i]
                dp_min[i] = dp_min[i - 1] + nums[i] - num
            else:
                dp_min[i] = dp_min[i - 1]

        for i in range(2*k-1, -1, -1):
            if nums[i] >= maxi:
                num = heapq._heappop_max(max_heap)
                heapq.heappush(max_heap, nums[i])
                heapq._heapify_max(max_heap)
                maxi = nums[i]
                dp_max[i] = dp_max[i + 1] + nums[i] - num
            else:
                dp_max[i] = dp_max[i + 1]

        res = float('inf')
        print(dp_max, dp_min)
        for i in range(k-1, n-k):
            res = min(res, dp_max[i] - dp_min[i+1])

        return res 


