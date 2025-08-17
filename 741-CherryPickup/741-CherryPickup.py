class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}

        def rec(r1, c1, c2):
            if (r1, c1, c2) in memo:
                return memo[(r1, c1, c2)]

            r2 = r1 + c1 - c2

            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return float("-inf")

            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")

            if r1 == c1 == n-1:
                return grid[r1][c1]

            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            next_cherries = max(
                rec(r1+1, c1, c2),
                rec(r1, c1+1, c2),
                rec(r1+1, c1, c2+1),
                rec(r1, c1+1, c2+1)
            )

            memo[(r1, c1, c2)] = cherries + next_cherries
            return memo[(r1, c1, c2)]
   
        return max(0, rec(0,0,0))

