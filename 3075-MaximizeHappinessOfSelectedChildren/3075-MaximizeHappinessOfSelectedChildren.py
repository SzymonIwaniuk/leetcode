import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        heapq._heapify_max(happiness)
        hap = 0
        for i in range(k):
            c = heapq._heappop_max(happiness)
            if c - i > 0:
                hap += c - i
            else:
                return hap

        return hap 

