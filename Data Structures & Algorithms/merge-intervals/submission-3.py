class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x:x[1], reverse = True)
        res = []
        l, r = 0, 1
        print(intervals)

        while r < len(intervals):
            curr = intervals[l]
            while r < len(intervals) and intervals[r][1] >= curr[0]:
                curr = [min(curr[0], intervals[r][0]), max(curr[1], intervals[r][1])]
                r += 1
            res.append(curr)
            l = r
        return res
        


            
