class Solution:
    def makeFancyString(self, s: str) -> str:
        tab = []

        prev1 = prev2 = None

        for ch in s:
            if ch != prev1 or ch != prev2:
                tab.append(ch)
            prev1, prev2 = ch, prev1

        return ''.join(tab)
                 

