class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_gap(l, bars):
            max_g = cur = prev = 1

            for b in bars:
                if b != prev + 1:
                    max_g = max(max_g, cur)
                    cur = 1

                cur += 1
                prev = b

            return max(max_g, cur)

        hBars.sort()
        vBars.sort()
        max_h = max_gap(n + 2, hBars)
        max_v = max_gap(m + 2, vBars)
        return min(max_h, max_v) ** 2
