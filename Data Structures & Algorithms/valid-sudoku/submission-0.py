from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # map absolute row index to set of nums
        rows = defaultdict(set)
        
        # map absolute col index to set of nums
        cols = defaultdict(set)

        # map square coord(0-2) to set of nums
        squares = defaultdict(set)


        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                square_coords = (row // 3, col // 3)
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in squares[square_coords]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                squares[square_coords].add(val)
        return True

