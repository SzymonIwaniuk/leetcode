class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple.sort(reverse = True)
        capacity.sort(reverse = True)

        b = 0

        for a in apple:
            while a:
                if a <= capacity[b]:
                    capacity[b] -= a
                    a = 0
                else:
                    a -= capacity[b]
                    capacity[b] = 0
                    b += 1

        return b + 1
