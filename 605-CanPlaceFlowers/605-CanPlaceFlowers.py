class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        
        if m == 1:
            if flowerbed[0] == 0:
                if n <= 1:
                    return True
            elif flowerbed[0] == 1:
                if n == 0:
                    return True

            return False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        
        for i in range(1, m-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True


        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        return True if n <= 0 else False