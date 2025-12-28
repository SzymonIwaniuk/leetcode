class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        r = n - 1
        c = 0

        while r != -1:
            while c < m and grid[r][c] >= 0:
                c += 1
            else:
                res += m - c
                r -= 1

        return res
