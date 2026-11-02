class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #directions 
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        #rows/cols
        ROWS, COLS = len(grid), len(grid[0])
        #minutes
        minutes = 0
        fresh_fruit = 0
        #queue
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_fruit += 1
        
        while queue: 
            if fresh_fruit == 0:
                return minutes
            minutes += 1
            for _ in range(len(queue)): 
                dr, dc = queue.popleft()
                for nr, nc in directions:
                    newR, newC = dr + nr, dc + nc
                    if newR >= 0 and newC  >= 0 and newR < ROWS and newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
                        fresh_fruit -= 1
    
                
        return 0 if fresh_fruit == 0 else -1






