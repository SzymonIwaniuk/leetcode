class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        diag = 0

        for x, y in dimensions:
            cur = sqrt(x**2 + y**2)
            if cur > diag:
                diag = cur
                area = x * y

            elif cur == diag:
                area = max(area, x * y)

        return area
