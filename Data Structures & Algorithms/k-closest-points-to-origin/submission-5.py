import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k nearest element
        min_points = []
        for x,y in points:
            heapq.heapify(min_points) # sort
            dist = round(((x ** 2) + (y ** 2))**(1/2), 10)
            if len(min_points) < k:
                min_points.append((-dist, [x,y]))
            elif dist < -(min_points[0][0]):
                heapq.heappop(min_points) # remove min elem
                heapq.heappush(min_points, (-dist, [x,y])) # add curr elem
        return [i[1] for i in min_points]

        