class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            seen = set()
            for j in range(9):
                curr = board[i][j]
                if curr != '.' and curr in seen:
                    return False
                seen.add(curr)
        
        for j in range(9):
            seen = set()
            for i in range(9):
                curr = board[i][j]
                if curr != '.' and curr in seen:
                    return False
                seen.add(curr)
        
        start = [(0,0), (3,0), (6,0), (0,3), (3,3), (6,3), (0,6), (3,6), (6,6)]
        for s in start:
            seen = set()
            for i in range(s[0], s[0]+3):
                for j in range(s[1], s[1]+3):
                    curr = board[i][j]
                    if curr != '.' and curr in seen:
                        return False
                    seen.add(curr)
        return True
                

        
        