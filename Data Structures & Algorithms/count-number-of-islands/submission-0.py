class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(curr, visited):
            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
            for n in neighbors:
                x,y = curr[0] + n[0], curr[1] + n[1]
                if not(0 <= x < row and 0 <= y < col):
                    continue
                else:
                    if grid[x][y] == '1' and (x,y) not in visited:
                        visited.add((x,y))
                        dfs((x,y), visited)
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs((i,j), visited)
                    res += 1

        return res


        