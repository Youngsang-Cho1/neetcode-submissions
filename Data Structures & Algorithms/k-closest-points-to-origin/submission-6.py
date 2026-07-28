import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k nearest element
        min_points = []
        for x,y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(min_points, (-dist, [x,y]))
        
            # pop the largest when len > k for every iteration
            if len(min_points) > k:
                heapq.heappop(min_points)
    
        return [i[1] for i in min_points]

        