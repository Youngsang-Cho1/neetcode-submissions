class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def bfs(coor):
            islands = deque()
            local_visited = set()
            islands.append(coor)
            local_visited.add(coor)

            while islands:
                curr = islands.popleft()
                neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
                for neighbor in neighbors:
                    x, y = curr[0] + neighbor[0], curr[1] + neighbor[1]
                    if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                        continue
                    if board[x][y] == 'O' and (x,y) not in local_visited:
                        local_visited.add((x,y))
                        islands.append((x,y))
            edge = False
            for cell in local_visited:
                x,y = cell
                if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) -1:
                    edge = True
            if not edge:
                for cell in local_visited:
                    x,y = cell
                    visited.add((x,y))
                    board[x][y] = 'X'
            else:
                visited.add((x,y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j] == 'O':
                    bfs((i,j))
        



                        

        