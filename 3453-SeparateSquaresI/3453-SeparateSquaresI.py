class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # bisection method
        eps = 1e-5
        low = min(y for _, y, l in squares)     
        high = max(y + l for _, y, l in squares)

        while high - low > eps:
            line = (high + low) / 2
            below = above = 0 
            for x, y, l in squares:
                if l + y <= line:
                    below += l*l
                elif y >= line:
                    above += l*l
                else:
                    below += (line - y) * l
                    above += (y + l - line) * l
                
            if above > below:
                low = line
            else:
                high = line

        return high

