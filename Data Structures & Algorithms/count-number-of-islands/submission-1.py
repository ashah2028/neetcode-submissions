class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #count islands 
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])


        #dfs each time new seen (seen = #2)
        def dfs(i, j):
            #boundaries
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == '0':
                return
            if grid[i][j] == '2':
                return
            #now change to seen
            grid[i][j] = '2'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            

        #iterate via each cell if not visited yet 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands

        