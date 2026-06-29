class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = 0
        while idx < len(matrix):
            row = matrix[idx]
            l = 0
            r = len(row) - 1
            if target == row[l] or target == row[r]:
                return True
            elif target > row[l] and target < row[r]:
                while l < r:
                    mid = (l + r) // 2
                    print(l, r, mid)
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
            idx += 1
        return False
                    

        
            





        