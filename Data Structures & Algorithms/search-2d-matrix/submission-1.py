class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1


        #Look for the row of target 
        while l <= r: 
            m = l + (r-l) // 2
            if target > matrix[m][COLS-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        
        if not (l <= r):
            return False
        row = (l + r) // 2
        #Look for pos in the row 
        l, r = 0, COLS - 1

        while l <= r:
            mp = l + (r - l) // 2
            if target > matrix[row][mp]:
                l  = mp + 1
            elif target < matrix[row][mp]:
                r = mp - 1
            else:
                return True
        return False

      
        