def bin_search(seq, enve, high):
    low = 0

    while low < high:
        mid = (low + high) // 2

        if seq[mid][1] >= enve[1]:
            high = mid

        else:
            low = mid + 1
    
    return low


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        
        n = len(envelopes)
        seq = [envelopes[0]]
        top = 1
        #print(envelopes)
        
        for i in range(1, n):
            if seq[-1][1] < envelopes[i][1]:
                seq.append(envelopes[i])
                top += 1

            else:
                idx = bin_search(seq, envelopes[i], top)
                seq[idx] = envelopes[i]
            #print(seq)

        return len(seq)

