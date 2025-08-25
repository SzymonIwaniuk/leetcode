class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        i = j = 0
        arr = []

        while i < m - 1 or j < n:
            i_c = i
            j_c = j

            tmp = []
            while i_c >= 0 and j_c < n:
                tmp.append(mat[i_c][j_c])
                i_c -= 1
                j_c += 1

            if (i + j) % 2 == 0:
                arr.extend(tmp)
            else:
                arr.extend(tmp[::-1])

            if i < m - 1:
                i += 1
            else:
                j += 1
             
        return arr

