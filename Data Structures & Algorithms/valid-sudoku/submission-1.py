class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #3 hashmaps - one for rows, cols, squares
        #Each row,col only have freq of one for each number
        #Square formula:  (row / 3) * 3 + (col / 3) for index of each square

        Rowfreq, Colfreq, Squarefreq = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in Rowfreq[r] 
                    or board[r][c] in Colfreq[c] 
                    or board[r][c] in Squarefreq[(r // 3, c //3)]):
                    return False
                Rowfreq[r].add(board[r][c])
                Colfreq[c].add(board[r][c])
                Squarefreq[( r // 3, c // 3)].add(board[r][c])

        return True

        
        