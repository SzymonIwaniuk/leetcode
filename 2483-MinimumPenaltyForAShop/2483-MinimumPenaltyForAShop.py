class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l = len(customers)
        pen = min_pen = 0
        time = -1

        for t in range(l):
            c = customers[t]
            pen += 1 if c == "Y" else -1
            if pen > min_pen:
                min_pen = pen
                time = t

        return time + 1
