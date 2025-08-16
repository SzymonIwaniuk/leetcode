from collections import deque 

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        queue, farthest = deque([0]), 0

        while queue:
            i = queue.popleft()
            start = max(i + minJump, farthest + 1)

            for j in range(start, min(i + maxJump + 1, n)):
                if s[j] == "0":
                    queue.append(j)
                    if j == n - 1:
                        return True
            farthest = i + maxJump
        
        return False


