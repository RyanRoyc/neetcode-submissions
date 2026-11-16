class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if (r//3, c//3) not in boxes:
                    boxes[(r//3, c//3)] = set()
                
                if num in rows[r] or num in cols[c] or num in boxes[(r//3, c//3)]:
                    return False
                
                boxes[(r//3, c//3)].add(num)
                rows[r].add(num)
                cols[c].add(num)
        
        return True
