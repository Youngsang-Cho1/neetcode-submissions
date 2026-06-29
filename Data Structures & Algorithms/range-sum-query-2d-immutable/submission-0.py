class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summation = 0
        for i in range(row1, row2 + 1):
            curr_elem = self.matrix[i]
            for j in range(col1, col2 + 1):
                summation += curr_elem[j]
        return summation

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)