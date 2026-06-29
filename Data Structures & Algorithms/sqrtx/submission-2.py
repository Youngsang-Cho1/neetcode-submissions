class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            result = x // mid
            if result == mid:
                return mid
            elif result > mid:
                left = mid + 1
            else:
                right = mid - 1

            print (result, mid, left, right)
        return right




        