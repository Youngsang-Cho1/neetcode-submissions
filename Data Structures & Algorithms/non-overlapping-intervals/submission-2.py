class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        temp = sorted(intervals, key = lambda x:x[1])
        res = 0
        
        l, r = 0, 1
        while r < len(temp):
            if temp[l][1] > temp[r][0]:
                res += 1
                r += 1
            else:
                l = r
                r += 1
        return res


