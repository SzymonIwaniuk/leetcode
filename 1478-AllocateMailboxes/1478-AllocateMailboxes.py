def calc_dist(arr):
    median = arr[len(arr)//2]
    return sum(abs(h - median) for h in arr)


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()      
        memo = {}
        
        medians = [[0] * n for _ in range(n)]
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            medians[i][i] = houses[i]
            cost[i][i] = 0
            for j in range(i + 1, n):
                medians[i][j] = houses[i + (j - i)//2]
                cost[i][j] = cost[i][j-1] + abs(houses[j] - medians[i][j])

        #print(cost)
        def rec(i, b):
            if b == 0:
                return 0 if i == n else float('inf')
            
            if (i, b) in memo:
                return memo[(i, b)]

            mini = float('inf')

            for j in range(i, n):
                mini = min(
                    mini,
                    cost[i][j] + rec(j + 1, b - 1)
                )
            
            memo[(i, b)] = mini
            #print(mini, (i, b))
            return mini
        
        return rec(0, k)
            
