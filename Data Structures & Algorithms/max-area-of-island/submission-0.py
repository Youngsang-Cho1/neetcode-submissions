from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        # dfs or bfs
        # bfs 
        # q, visited. add grid[0][0]
        # bfs(curr, visited)
        # area = 1
        # while q:
            # pop
            # neighbors
            # if grid[x][y] == 1 and not in visited
                # add q, add visited
                # area += 1
            #return area
        
        def bfs(curr):
            total_area = 1
            visited.add(curr)
            one_islands = deque()
            one_islands.append(curr)
            while one_islands:
                length = len(one_islands)
                for _ in range(length):
                    cell = one_islands.popleft()
                    #print(cell)
                    neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
                    for neighbor in neighbors:
                        x, y = cell[0] + neighbor[0], cell[1] + neighbor[1]
                        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                            continue
                        if grid[x][y] == 1 and (x,y) not in visited:
                            visited.add((x,y))
                            one_islands.append((x,y))
                            total_area += 1
            return total_area
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and (x,y) not in visited:
                    curr_area = bfs((x,y))
                    res = max(res, curr_area)
        return res
                
                            
                    


            
        