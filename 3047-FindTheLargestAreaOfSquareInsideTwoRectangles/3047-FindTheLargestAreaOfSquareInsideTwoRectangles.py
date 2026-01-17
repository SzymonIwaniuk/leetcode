class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        maxi = 0

        def area(i, j):
            xibl, yibl = bottomLeft[i]
            xitr, yitr = topRight[i]
            xjbl, yjbl = bottomLeft[j]
            xjtr, yjtr = topRight[j]
            
            w = min(xitr, xjtr) - max(xibl, xjbl)
            h = min(yitr, yjtr) - max(yibl, yjbl)

            if w > 0 and h > 0:
                return min(w, h) ** 2

            return 0 
            
        for i in range(n - 1):
            for j in range(i + 1, n):
                maxi = max(area(i, j), maxi)

        return maxi
