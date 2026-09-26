from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        level = 0
        alive_count = 0

        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    alive_count += 1

        neighbors = [(0,1), (0,-1), (1,0), (-1,0)]

        while q and alive_count > 0:
            length = len(q)
            for _ in range(length):
                curr = q.popleft()
                for n in neighbors:
                    x, y = curr[0] + n[0], curr[1] + n[1]
                    if not (0 <= x < row and 0 <= y < col):
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        alive_count -= 1
                        q.append((x, y))
            level += 1
        if alive_count > 0:
            return -1
        return level