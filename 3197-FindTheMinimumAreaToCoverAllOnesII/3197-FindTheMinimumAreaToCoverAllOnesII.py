def find_cover(ll, lr, lt, lb, grid):
    top, bot, left, right = float('inf'), -1, float('inf'), -1

    for i in range(lt, lb):
        for j in range(ll, lr):
            if grid[i][j] == 1:
                top = min(top, i)
                bot = max(bot, i)
                left = min(left, j)
                right = max(right, j)

    if bot == -1:
        return 0

    return (bot - top + 1) * (right - left + 1)
        

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = float('inf')

        # 3 divisions verticaly
        for i in range(1, m-1):
            for j in range(i+1, m):
                a = find_cover(0, i, 0, n, grid)
                b = find_cover(i, j, 0, n, grid)
                c = find_cover(j, m, 0, n, grid)
                res = min(res, a + b + c)

#    +---+---+---+
#    |   |   |   |
#    |   |   |   |
#    |   |   |   |
#    +---+---+---+

        # 3 divisions horizontally 
        for i in range(1, n-1):
            for j in range(i+1, n):
                # left, right, top, bot
                a = find_cover(0, m, 0, i, grid)
                b = find_cover(0, m, i, j, grid)
                c = find_cover(0, m, j, n, grid)
                res = min(res, a + b + c)

#    +---------+
#    |         |
#    +---------+
#    |         |
#    +---------+
#    |         |
#    +---------+

        for i in range(1, n):
            for j in range(1, m):
                # left, right, top, bot
                # 1 case
                a = find_cover(0, j, 0, i, grid)
                b = find_cover(j, m, 0, i, grid)
                c = find_cover(0, m, i, n, grid)
                res = min(res, a + b + c)
                # 2 case
                a = find_cover(0, j, i, n, grid)
                b = find_cover(j, m, i, n, grid)
                c = find_cover(0, m, 0, i, grid)
                res = min(res, a + b + c)
                # 3 case
                a = find_cover(j, m, 0, i, grid)
                b = find_cover(j, m, i, n, grid)
                c = find_cover(0, j, 0, n, grid)
                res = min(res, a + b + c)
                # 4 case
                a = find_cover(0, j, 0, i, grid)
                b = find_cover(0, j, i, n, grid)
                c = find_cover(j, m, 0, n, grid)
                res = min(res, a + b + c)

        return res

# 1 case
# +---------+
# |    |    |
# +---------+
# |    |    |
# +---------+
# |         |
# +---------+
# 2 case
# +---------+
# |         |
# +---------+
# |    |    |
# +---------+
# |    |    |
# +---------+
# 3 case
# +---+-------+
# |   |       |
# |   |       |
# +---+---+---+
# |   |       |
# |   |       |
# +---+---+---+
# 4 case
# +---+---+---+
# |       |   |
# |       |   |
# +---+---+---+
# |       |   |
# |       |   |
# +-------+---+



