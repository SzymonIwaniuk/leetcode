class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        if n == 1:
            return True
        
        elif n > 1 and stones[1] > 1:
            return False

        mapping = {stones[i]: i for i in range(n)}
        dp = [[-1] * (n + 1) for _ in range(n)]

        dp[0][0] = 1
        dp[1][1] = 1

        for i in range(1, n):
            for j in range(1, i + 1):
                if dp[i][j] > 0:
                    jump = dp[i][j]
                    for k in range(jump - 1, jump + 2):
                        if mapping.get(k + stones[i], False):
                            dp[mapping[k + stones[i]]][i] = k

        # for i in range(1, n):
        #     print(dp[i])
        for i in range(n + 1):
            if dp[-1][i] > -1:
                return True

        return False
                    
