"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for idx, interval in enumerate(intervals):
            events.append((interval.start, 'start', idx))
            events.append((interval.end, 'end', idx))
        
        events.sort()
        active = set()
        idx = 0
        res = 0
        while idx < len(events):
            curr_time, is_start, id_num = events[idx]
            
            if is_start == 'start':
                active.add(id_num)
            
            elif is_start == 'end':
                res = max(res, len(active))
                active.remove(id_num)
            idx += 1
        return res


            
        