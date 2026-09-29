class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_interval = newInterval
        combined = []
        inserted = False

        for interval in intervals:
            start, end = interval
            if new_interval[0] <= end and start <= new_interval[1]:
                new_interval = [min(start, new_interval[0]), max(end, new_interval[1])]
            elif end < new_interval[0]:
                combined.append(interval)
            
            elif start > new_interval[1]:
                if not inserted:
                    combined.append(new_interval)
                    inserted = True
                combined.append(interval)
        if not inserted:
            combined.append(new_interval)
        return combined
                
            
        





