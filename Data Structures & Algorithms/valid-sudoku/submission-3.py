class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        sq_dict = {}
        # row
        for i in board:
            for j in i:
                if (j != '.') and  (j not in row_dict.keys()):
                    row_dict[j] = 1
                elif (j != '.') and  (j in row_dict.keys()):
                    return False
            row_dict = {}

        # col
        for i in range(0,9):
            cols = []
            for j in range(0,9):
                cols.append(board[j][i]) # add all col elements

            for k in cols:
                if (k != '.') and (k not in col_dict.keys()):
                    col_dict[k] = 1
                elif (k != '.') and (k in col_dict.keys()):
                    return False

            col_dict = {}

# [sq] = {4:1, 1:1...}
        # square
        for row in range(0,9):
            for col in range(0,9):
                square = ((row // 3), col // 3) # square index (set)
                if square not in sq_dict.keys():
                    sq_dict[square] = {}

                if (board[row][col] != '.') and (board[row][col] not in sq_dict[square]):
                    sq_dict[square][board[row][col]] = 1
                elif (board[row][col] != '.') and (board[row][col] in sq_dict[square]):
                    return False
        return True
