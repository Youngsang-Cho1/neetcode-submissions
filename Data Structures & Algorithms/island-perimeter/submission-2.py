class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 1
            elif (i,j) in visited:
                return 0
            visited.add((i,j))
            perim = dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return perim
            
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j]:
                    return dfs(i,j)
            
    
    # first, global set or list
    # second, implement dfs with recursion
    # if grid is at the border or is 0 return 1
        