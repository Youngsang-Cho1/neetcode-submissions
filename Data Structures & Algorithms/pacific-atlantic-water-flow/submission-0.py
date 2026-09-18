class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        def dfs(node, visited):
            visited.add(node)
            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
            for n in neighbors:
                x,y = node[0] + n[0], node[1] + n[1]
                if not 0 <= x < len(heights) or not 0 <= y < len(heights[0]):
                    continue
                elif (x,y) not in visited and heights[node[0]][node[1]] <= heights[x][y]:
                    visited.add((x,y))
                    dfs((x,y), visited)
        row, col = len(heights), len(heights[0])

        for i in range(col):
            dfs((0,i), pacific)
        
        for i in range(row):
            dfs((i,0), pacific)

        for i in range(col):
            dfs((row - 1,i), atlantic)
        
        for i in range(row):
            dfs((i, col - 1), atlantic)
        return list(pacific & atlantic)




        
        


        
        