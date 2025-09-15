from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        minheap = []

        for i in range(n):
            pas = classes[i][0]
            total = classes[i][1]
            gain = ((pas + 1) * total - pas * (total + 1)) / ((total + 1) * total) 

            heappush(minheap, (-gain, i))

            print(gain)

        
        for i in range(extraStudents):
            gain, idx = heappop(minheap)

            classes[idx][0] += 1
            classes[idx][1] += 1
            pas = classes[idx][0]
            total = classes[idx][1]
            gain = ((pas + 1) * total - pas * (total + 1)) / ((total + 1) * total)
            heappush(minheap, (-gain, idx))

        res = 0
