from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP O(n^2)

        # n = len(nums)
        # inf = 10e10

        # dp = [inf] * n
        # dp[0] = 0

        # for i in range(n):
        #     for j in range(i + 1, min(nums[i] + i + 1, n)):
        #         dp[j] = min(dp[j], dp[i] + 1)
        
        # print(dp)
        # return dp[-1]

        # BFS greedy approach 
        # O(V + E)
        n = len(nums)
        visited = [float('inf')] * n 

        if n == 1:
            return 0

        queue = deque()
        
        for i in range(min(nums[0], n - 1), 0, -1):
            # (jumps, index)
            queue.append((1, i)) 

        while queue:
            jumps, index = queue.popleft()

            if index == n - 1:
                return jumps

            for i in range(min(nums[index] + index, n - 1), index, -1):
                if visited[i] > jumps + 1:
                    visited[i] = jumps + 1
                    queue.append((jumps + 1, i))

