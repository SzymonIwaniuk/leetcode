from bisect import bisect_left

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        l = len(events)
        events.sort(key = lambda x: x[0])
        
        memo = {}

        def rec(i, q):
            if (i, q) in memo:
                return memo[(i, q)]

            if i == l or q == 2:
                return 0

            idx = bisect_left(
                events,
                events[i][1] + 1, 
                lo = i + 1, 
                hi = l, 
                key = lambda x: x[0]
            )
            maxi = max(events[i][2] + rec(idx, q + 1), rec(i + 1, q))
            memo[(i, q)] = maxi
            return maxi

        return rec(0, 0)
