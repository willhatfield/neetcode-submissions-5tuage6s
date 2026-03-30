class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        for r in range(n):
            col = set()
            for num in board[r]:
                if num in col:
                    return False
                elif num != '.':
                    col.add(num)
        
        for c in range(n):
            row = set()
            for i in range(n):
                num = board[i][c]
                if num in row:
                    return False
                elif num != '.':
                    row.add(num)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = board[r][c]
                        if num in box:
                            return False
                        elif num != '.':
                            box.add(num)
        
        return True
