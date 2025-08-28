class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        out = [[None] * n for _ in range(n)]
        
        j = 0
        while j < n:
            i = 0
            nj = j
            tmp = []
            while nj < n and i < n:
                tmp.append(grid[nj][i])
                nj += 1
                i += 1

            tmp.sort()
            k = 0
            nj -= 1
            i -= 1
            while nj >= j and i >= 0:
                out[nj][i] = tmp[k]
                nj -= 1
                i -= 1
                k += 1

            j += 1


        j = 1
        while j < n:
            i = 0
            nj = j
            tmp = []
            while nj < n and i < n:
                tmp.append(grid[i][nj])
                nj += 1
                i += 1

            tmp.sort(reverse=True)
            k = 0
            nj -= 1
            i -= 1
            while nj >= j and i >= 0:
                out[i][nj] = tmp[k]
                nj -= 1
                i -= 1
                k += 1

            j += 1

        return out