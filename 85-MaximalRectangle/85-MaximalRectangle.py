class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix) ; m = len(matrix[0])
        dp = [0 for _ in range(m)]
        result = 0

        for i in range(n):
            for j in range(m):
                if int(matrix[i][j]):
                    dp[j] += 1
                else:
                    dp[j] = 0
            
            stack = []
            for j in range(m + 1):
                cur = dp[j] if j < m else 0
                while stack and cur < (h := dp[stack[-1]]):
                    stack.pop()
                    # width
                    w = j if not stack else j - stack[-1] - 1
                    result = max(result, h * w)
                stack.append(j)

        return result   

                    
            
