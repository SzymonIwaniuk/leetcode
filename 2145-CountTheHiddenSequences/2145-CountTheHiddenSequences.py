class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # first = 0
        n = len(differences)
        arr = [0] * (n + 1)

        for i in range(n):
            arr[i + 1] = differences[i] + arr[i]

        r = max(arr) - min(arr)
        out = upper - lower  - r + 1
        return out if out > 0 else 0 
