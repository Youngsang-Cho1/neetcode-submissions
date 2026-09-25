from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        level = 0
        banana_count = 0
        rotten_count = 0
        alive_count = 0
        row, col = len(grid), len(grid[0])

        for i in range((row)):
            for j in range((col)):
                if grid[i][j] == 2:
                    q.append((i,j))
                    rotten_count += 1
                elif grid[i][j] == 1:
                    alive_count += 1
        if alive_count == 0 and rotten_count > 0:
            return 0
        banana_count = alive_count + rotten_count

        while q:
            length = len(q)
            if len(visited) == banana_count:
                    return level
            for _ in range(length):
                curr = q.popleft()
                visited.add(curr)
                neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
                for n in neighbors:
                    x, y = curr[0] + n[0], curr[1] + n[1]
                    if not (0 <= x < row and 0 <= y < col):
                        continue
                    elif grid[x][y] == 1 and (x,y) not in visited:
                        visited.add((x,y))
                        q.append((x,y))
            level += 1
        
        if len(visited) != banana_count:
            return -1
        return level
                    


        
        