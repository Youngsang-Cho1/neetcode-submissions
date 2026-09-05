class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        top, bottom = -1, row
        left, right = -1, col
        res = []
        x, y = 0, 0
        counter = 0
        while counter < (row * col):
            print(counter)
            while y < right:
                res.append(matrix[x][y])
                counter += 1
                y += 1
            if counter == (row * col):
                break
            x += 1
            y -= 1
            top += 1

            while x < bottom:
                res.append(matrix[x][y])
                counter += 1
                x += 1
            if counter == (row * col):
                break
            
            x -= 1
            y -= 1
            right -= 1


            while y > left:
                res.append(matrix[x][y])
                counter += 1
                y -= 1
            if counter == (row * col):
                break
            x -= 1
            y += 1
            bottom -= 1

            while x > top:
                res.append(matrix[x][y])
                counter += 1
                x -= 1
            if counter == (row * col):
                break
            x += 1
            y += 1
            left += 1
        return res


                

        