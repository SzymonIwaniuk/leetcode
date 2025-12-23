from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0

        def helper(n):
            if n == 1:
                return -1
            if n == 2 or n == 3:
                return 1
            if n % 3 == 1:
                rounds = 2 + ((n - 4) // 3)
            elif n % 3 == 2:
                rounds = 1 + ((n - 2) // 3)
            else:
                rounds = n // 3
            return rounds
        

        for n in count.values():
            cur = helper(n)
            if cur != -1:
                ans += cur
            else:
                return cur

        return ans
