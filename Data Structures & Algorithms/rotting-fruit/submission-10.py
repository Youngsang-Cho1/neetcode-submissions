from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        row, col = len(grid), len(grid[0])
        fruit_total = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fruit_total += 1
                elif grid[i][j] == 2:
                    fruit_total += 1
                    rotten.append((i,j))
    
        #print(rotten)
        visited = set()
        for fruit in rotten:
            visited.add(fruit)

        minute = 0

        while rotten and len(visited) < fruit_total:
            count = len(rotten)
            for _ in range(count):
                curr = rotten.popleft()
                neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
                for n in neighbors:
                    x,y = curr[0] + n[0], curr[1] + n[1]
                    if not (0 <= x < row and 0 <= y < col):
                        continue
                    if grid[x][y] == 1 and (x,y) not in visited:
                        grid[x][y] = 2
                        rotten.append((x,y))
                        visited.add((x,y))
            minute += 1
        print(visited)
        if len(visited) < fruit_total:
            return -1
        return minute
                    

        