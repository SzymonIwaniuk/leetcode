
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) ; m = len(word2)
        memo = {}

        def rec(i, j): 
            if (i, j) in memo:
                return memo[(i, j)]

            if n == i and m == j:
                return 0
        
            if i < n and m == j:
                return n - i
            
            if j < m and n == i:
                return m - j
            
            else:
                mini = float("inf")

                if word1[i] == word2[j]:
                    mini = rec(i + 1, j + 1)

                else:
                    # delete, replace, insert
                    mini = min(mini, rec(i + 1, j) + 1, rec(i + 1, j + 1) + 1, rec(i, j + 1) + 1)

            memo[(i, j)] = mini
            return mini

        return rec(0, 0)
