class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        start_iszero = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        start_iszero = 1
                    else:
                        matrix[i][0] = 0
                        
        

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(row):
                matrix[i][0] = 0
        if start_iszero:
            for j in range(col):
                matrix[0][j] = 0 




                
        

        

        
        