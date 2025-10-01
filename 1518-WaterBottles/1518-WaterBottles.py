class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0 
        empty_bottles = 0

        while numBottles > 0:
            res += numBottles
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange

        return res
