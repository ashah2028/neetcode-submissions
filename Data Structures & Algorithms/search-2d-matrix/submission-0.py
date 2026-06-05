class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #approach have 2 pointers one for rows, one for columns
        Rows, Cols = len(matrix), len(matrix[0])
        #two pointers
        l, r = 0, Rows - 1
        while l <= r:
            row = (l + r) // 2
            if matrix[row][-1] < target:
                l = row + 1
            elif matrix[row][0] > target:
                r = row - 1
            else:
                break
        if not (l <= r):
            return False
        row = (l + r) // 2
        #Now we have found the row the result may be on
        rw, col = 0, Cols - 1
        while rw <= col:
            val = (rw + col) // 2
            if matrix[row][val] < target: 
                rw = val + 1
            elif matrix[row][val] > target:
                col = val -1
            else:
                return True
        return False

        