class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(row):
            for j in range(col): 
                if i in zero_rows:
                    matrix[i][j] = 0
                elif j in zero_cols:
                    matrix[i][j] = 0


                
        

        

        
        