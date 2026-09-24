class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        from collections import deque
        row, col = len(grid) - 1, len(grid[0]) - 1
        res = -1
        q = deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        level = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == (row, col):
                    return level
                neighbors = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
                for n in neighbors:
                    x, y = curr[0] + n[0], curr[1] + n[1]
                    if not (0 <= x <= row and 0 <= y <= col):
                        continue
                    if grid[x][y] == 0 and ((x,y)) not in visited:
                        visited.add((x,y))
                        q.append((x,y))
            level += 1
    
        return res
        
        