class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Run through each cell
        #When you get to a land cell, dfs in each direction
        #Keep boolean parameter and count:
            #Start false
            #If true, assign min count of all the dfs returned
            #If false (out of bounds, no chest, or water) stay false
            #If no dfs true, do not resassign

        ROWS, COLS = len(grid), len(grid[0])
        #find treasures
        que = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    que.append((r, c))
        directions = [(1, 0), (0, 1), (-1 , 0), (0, -1)]
        while que:
            r, c = que.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < ROWS and nr >= 0 and nc >= 0 and nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    que.append((nr, nc))



        