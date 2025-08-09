class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Edge case
        if n == 0:
            return False

        bin_str = str(bin(n))
        l = len(bin_str[3:])

        if bin_str[3:] == l  * '0':
            return True

        return False 
