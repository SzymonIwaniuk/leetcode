class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # O(nm)
        n = len(grid)
        m = len(grid[0])
        height = width = 0
        top, bot, left, right = float('inf'), 0, float('inf'), 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bot = max(bot, i)
                    left = min(left, j)
                    right = max(right, j)

        return (bot - top + 1) * (right - left + 1)
        
