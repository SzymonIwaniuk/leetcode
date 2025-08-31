class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    if board[i][j] not in rows[i]:
                        rows[i].add(board[i][j])

                    else:
                        return False
                    
                    if board[i][j] not in boxes[box]:
                        boxes[box].add(board[i][j])

                    else:
                        return False

                if board[j][i] != '.':
                    if board[j][i] not in cols[i]:
                        cols[i].add(board[j][i])

                    else:
                        return False


        return True
