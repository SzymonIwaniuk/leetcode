class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        cnt_t = {tops[0]:0, bottoms[0]:0}
        cnt_b = {tops[0]:0, bottoms[0]:0}
        both = {tops[0]:0, bottoms[0]:0}

        for i in range(n):
            if tops[i] in cnt_t:
                cnt_t[tops[i]] += 1
            if bottoms[i] in cnt_t:
                cnt_b[bottoms[i]] += 1
                if tops[i] == bottoms[i]:
                    both[bottoms[i]] += 1
        poss = []
        for k in cnt_t.keys():
            if cnt_t[k] + cnt_b[k] - both[k] == n:
                poss.append(min(n-cnt_t[k], n-cnt_b[k]))

        return min(poss) if poss else -1
        
