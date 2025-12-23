import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # 1. loop through list till profit <= w adding to max heap (-profits)
        # 2. we stop
        # 3. we must add at least one biggest element from heap and reduce k
        # 4. continue looping
        # 5. We add elements from heap till k == 0 or empty.

        n = len(profits)
        pairs = sorted(list(zip(capital, profits)), key = lambda x: (x[0], x[1]))
        heap = []
        i = 0
        while i < n:
            if pairs[i][0] <= w:
                heapq.heappush(heap, (-pairs[i][1], pairs[i][0]))
                i += 1
            else:
                if k > 0 and heap:
                    val, _ = heapq.heappop(heap)
                    w -= val
                    k -= 1

                else:
                    break

        while k and heap:
            val, _ = heapq.heappop(heap)
            w -= val
            k -= 1

        return w
