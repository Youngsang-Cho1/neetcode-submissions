from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        valid_cell = (2 ** 31) - 1
        row, col = len(grid), len(grid[0])
        start = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    start.append((i,j))
        #print(start)
        lands = deque()
        for cell in start:
            lands.append(cell)

        while lands:
            length = len(lands)
            for _ in range(length):
                curr = lands.popleft()
                neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
                for n in neighbors:
                    x,y = curr[0] + n[0], curr[1] + n[1]
                    if not (0 <= x < row and 0 <= y < col):
                        continue
                    if grid[x][y] == -1:
                        continue
                    if grid[x][y] == valid_cell:
                        grid[x][y] = grid[curr[0]][curr[1]] + 1
                        lands.append((x,y))

                


        



        