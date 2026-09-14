class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key = lambda x:x[1], reverse = True)
        #print(intervals)
        res = []
        idx = 1
        prev = intervals[0]
        while idx < len(intervals):
            if intervals[idx][1] >= prev[0]:
                while idx < len(intervals) and intervals[idx][1] >= prev[0]:
                    prev = [min(intervals[idx][0], prev[0]), max(intervals[idx][1], prev[1])]
                    idx += 1
                
            else:
                res.append(prev)
                prev = [intervals[idx][0], intervals[idx][1]]
                idx += 1
        res.append(prev)

        return res