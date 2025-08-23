class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = matrix[0].count(1)
        
        for i in range(1, n):
            res += matrix[i][0]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1],
                    ) + 1
                res += matrix[i][j]

        return res
        
