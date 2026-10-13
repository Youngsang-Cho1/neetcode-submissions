from collections import deque
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for start, end, weight in times:
            graph[start].append((end, weight))
        
        minheap = [(0, k)]
        distances = {i : float('inf') for i in range(1, n+1)}
        distances[k] = 0
        
        while minheap:
            curr_dist, curr_node = heapq.heappop(minheap)
            if curr_dist > distances[curr_node]:
                continue
            for neighbor, neighbor_dist in graph[curr_node]:
                dist = curr_dist + neighbor_dist
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(minheap, (dist, neighbor))


        res = max(distances.values())
        return res if res != float('inf') else -1


        