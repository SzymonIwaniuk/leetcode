class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        prev_1 = prev_2 = None
        maxi = -1

        for i in range(n):
            curr = int(num[i])
            if curr == prev_1 == prev_2 and curr > maxi:
                maxi = curr

            prev_1, prev_2 = curr, prev_1
        
        return "" if maxi == -1 else 3 * str(maxi)

                


