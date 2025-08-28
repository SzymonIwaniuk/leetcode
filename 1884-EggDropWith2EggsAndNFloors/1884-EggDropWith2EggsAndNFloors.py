from math import ceil

class Solution:
    def twoEggDrop(self, n: int) -> int:
        return int(ceil((1 + sqrt(1 + 8*n)) / 2) - 1)
        