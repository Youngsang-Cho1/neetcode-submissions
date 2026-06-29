class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        sq_dict = {}
        # row
        for i in board:
            for j in i:
                if j not in row_dict.keys():
                    row_dict[j] = 1
                else:
                    row_dict[j] += 1
            row_dict['.'] = 0
            if 2 in row_dict.values():
                return False
            row_dict = {}

        # col
        for i in range(0,9):
            cols = []
            for j in range(0,9):
                cols.append(board[j][i])

            for k in cols:
                if k not in col_dict.keys():
                    col_dict[k] = 1
                else:
                    col_dict[k] += 1
            col_dict['.'] = 0
            if 2 in col_dict.values():
                return False
            col_dict = {}

# [sq] = {4:1, 1:1...}
        # square
        for row in range(0,9):
            for col in range(0,9):
                square = ((row // 3), col // 3)
                sq_values = {}
                if square not in sq_dict.keys():
                    sq_dict[square] = {}

                if (board[row][col] != '.') and (board[row][col] not in sq_dict[square]):
                    sq_dict[square][board[row][col]] = 1
                elif (board[row][col] != '.') and (board[row][col] in sq_dict[square]):
                    sq_dict[square][board[row][col]] += 1
        print (sq_dict)
        for i in sq_dict.values():
            for j in i.values():
                if int(j) > 1:
                    return False

        return True
