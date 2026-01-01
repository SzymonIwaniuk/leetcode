class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(lambda x: int(x),list(str(sum(d * 10**i for i, d in enumerate(reversed(digits))) + 1))))
