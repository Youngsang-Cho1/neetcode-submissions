class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        def row_col_zeros(coor):
            x,y = coor
            for i in range(row):
                matrix[i][y] = 0
            for i in range(col):
                matrix[x][i] = 0
        coors = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    coors.append((i,j))
        for coor in coors:
            row_col_zeros(coor)
        

        

        
        