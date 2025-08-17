class Solution:
    def trap(self, height: List[int]) -> int:
        # O(nm)
        # n = len(height)
        # m = max(height)
        # score = 0

        # for i in range(1, m + 1):
        #     prev = None
        #     for j in range(n):
        #         if height[j] >= i:
        #             if prev == None:
        #                 prev = j
        #             else:
        #                 score += j - prev - 1
        #                 prev = j

        # return score

        # Better approach O(n)

        n = len(height)
        water = 0
        # Max height of each bar from left to current inclusive
        dp1 = [0] * n
        dp1[0] = height[0]

        # Max height of each bar rom right to current inclusive
        dp2 = [0] * n
        dp2[-1] = height[-1]

        for i in range(1, n):
            dp1[i] = max(dp1[i-1], height[i])
            dp2[-i-1] = max(dp2[-i], height[-i-1])
            # print(-i - 1) 
        
        # print(dp1, dp2)
        # Calculate water
        for i in range(n):
            dp1[i] = min(dp1[i], dp2[i])
            water += dp1[i] - height[i]

        return water
