
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        xc, yc = points[0]

        for x, y in points[1:]:
            time += max(abs(xc - x), abs(yc - y))
            xc, yc = x, y

        return time

