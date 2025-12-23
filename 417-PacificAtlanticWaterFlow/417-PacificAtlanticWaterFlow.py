class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights) ; m = len(heights[0])
        visited_pac = [[False] * m for _ in range(n)]
        visited_atl = [[False] * m for _ in range(n)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, visited):
            for x, y in moves:
                if 0 <= i + x < n and \
                    0 <= j + y < m and \
                    visited[i + x][j + y] is False and \
                    heights[i][j] <= heights[i + x][j + y]:
                        visited[i + x][j + y] = True
                        dfs(i + x, j + y, visited)
           
        for i in range(n):
            visited_pac[i][0] = True
            visited_atl[i][m-1] = True
            dfs(i, 0, visited_pac)
            dfs(i, m-1, visited_atl)

        for j in range(m):
            visited_pac[0][j] = True
            visited_atl[n-1][j] = True
            dfs(0, j, visited_pac)
            dfs(n-1, j, visited_atl)

        cells = []
        for i in range(n):
            for j in range(m):
                if visited_pac[i][j] and visited_atl[i][j]:
                    cells.append([i,j])

        return cells

