class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        l = n + m
        arr = [None] * l
        i = j = 0

        while i < n or j < m:
            if i < n:
                arr[i+j] = word1[i]
                i += 1

            if j < m:
                arr[i+j] = word2[j]
                j += 1

        return "".join(arr)  
