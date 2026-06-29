class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            print(l, r)
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        if not(l <= r):
            return False

        row = matrix[mid]
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if target == row[mid]:
                return True
            elif target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False

        