from heapq import heappush, heappop


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        inf = float('inf')
        times = [[[inf] * 2 for _ in range(m)] for __ in range(n)]
        times[0][0][0] = 0
        queue = [(0, 1, 0, 0)] # time, move, i, j
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            time, move, i, j = heappop(queue)
            
            if time > times[i][j][move-1]:
                continue

            new_move = 2 if move == 1 else 1

            for x, y in moves:
                if 0 <= i + x < n and 0 <= j + y < m:
                    new_time = max(time, moveTime[i+x][j+y]) + move
                
                    if new_time < times[i+x][j+y][new_move-1]:
                        times[i+x][j+y][new_move-1] = new_time
                        heappush(queue, (new_time, new_move, i+x, j+y))


        return min(times[n-1][m-1])
