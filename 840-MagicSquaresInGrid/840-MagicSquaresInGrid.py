def is_magic(i, j, grid):
    tab = [0] * 8 
    nums = set()

    for r in range(3):
        for c in range(3):
            if grid[i+r][j+c] > 9 or \
            grid[i+r][j+c] < 1 or \
            grid[i+r][j+c] in nums:
                return False

            nums.add(grid[i + r][j + c])
            tab[r] += grid[i + r][j + c]
            tab[3 + c] += grid[i + r][j + c]

            if r == c:
                tab[6] += grid[i + r][j + c]
                
            if r + c == 2:
                tab[7] += grid[i + r][j + c]
    
    return all(map(lambda x: x == 15, tab))


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n - 2):
            for j in range(m - 2):
                if is_magic(i, j, grid):
                    res += 1
        
        return res
