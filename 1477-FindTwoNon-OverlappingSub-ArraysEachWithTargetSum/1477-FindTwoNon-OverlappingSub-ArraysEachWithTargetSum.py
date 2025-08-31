from heapq import heappush, heappop

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        res = float('inf')
        cur_sum = 0
        min_len = [float('inf')] * n
        i = 0

        for j in range(n):
            cur_sum += arr[j]

            while cur_sum > target and i <= j:
                cur_sum -= arr[i]
                i += 1

            if cur_sum == target:
                length = j - i + 1
                if i > 0:
                    res = min(res, length + min_len[i-1])
                min_len[j] = length
            

            if j > 0:
                min_len[j] = min(min_len[j-1], min_len[j])

        return res if res != float('inf') else -1
