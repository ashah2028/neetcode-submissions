class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #edge cases: what happens if no bananas? can the grid be empty? 
        #Thinking about a bfs approach -> start from the rotten fruit
        ROWS, COLS = len(grid), len(grid[0])
        #initalize a queue 
        q = collections.deque()
        fresh = 0
        minutes = 0
        #get rotten fruit:
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0, 1],[0, -1], [1, 0], [-1, 0]]
        #iterate through the queue:

        while fresh > 0 and q:
            length = len(q)
            #need to pop by level -> for loop
            for i in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < ROWS and r >= 0 and c < COLS and c >= 0 and grid[r][c] == 1:
                        #turn rotten and append to queue
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1

            
