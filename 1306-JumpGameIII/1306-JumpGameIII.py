class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = set()

        def rec(i):
            if i >= 0 and i < n and i not in seen: 
                seen.add(i)
                jump = arr[i]

                if jump == 0:
                    return True
            
                return rec(i + jump) or rec(i - jump)
            return False

        return rec(start)

