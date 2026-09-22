class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        coor = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    coor.append((i,j))
       # dfs
        def dfs(curr, visited, idx):
            if idx == len(word):
                return True
            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
            for n in neighbors:
                x,y = curr[0] + n[0], curr[1] + n[1]
                if not(0 <= x < len(board) and 0 <= y < len(board[0])):
                    continue
                if word[idx] == board[x][y] and (x,y) not in visited:
                    visited.add((x,y))
                    if dfs((x,y), visited, idx + 1):
                        return True
                    visited.remove((x,y))
            return False

        for c in coor:
            visited = {c}
            if dfs(c, visited, 1):
                return True
        return False




    