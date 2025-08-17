def reconstruction(str1, str2, n, m, L):
        i, j = n, m
        result = []
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1

            elif L[i-1][j] > L[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1
        
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        return ''.join(result[::-1])



class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Article about longest common subsequence
        https://www.geeksforgeeks.org/dsa/python-program-for-longest-common-subsequence/
        """

        n = len(str1)
        m = len(str2)

        L = [[None]*(m + 1) for i in range(n + 1)] 

        for i in range(n + 1): 
            for j in range(m + 1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif str1[i-1] == str2[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j], L[i][j-1]) 

        superseq = reconstruction(str1, str2, n, m, L)
        return superseq
