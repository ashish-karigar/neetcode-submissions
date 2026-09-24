class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key: (r//3,c//3)
        length = len(board)

        for r in range(length):
            for c in range(length):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or
                 board[r][c] in cols[c] or 
                 board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
        
        
            
        