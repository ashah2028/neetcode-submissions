class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #lets try bfs: 


        #need a queue (initalize in bfs)
        #need island counter 
        islands = 0
        #directions
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        #rows and cols 
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue: 
                dr, dc = queue.popleft()
                if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS or grid[dr][dc] !='1':
                    continue
                grid[dr][dc] = '0'
                for nr, nc in directions:
                    queue.append((dr + nr, dc + nc))
            return


        #still loop through each choice and go through bfs if #1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands

