class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # extract each row
        rows = [set() for _ in range(9)]
        # extract each column
        columns = [set() for _ in range(9)]
        # extract each box
        boxes = [set() for _ in range(9)]
        # check for duplicates
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r // 3) * 3 + (c // 3)
                if value in rows[r] or value in columns[c] or value in boxes[box]:
                    return False
                rows[r].add(value)
                columns[c].add(value)
                boxes[box].add(value)
        return True 

