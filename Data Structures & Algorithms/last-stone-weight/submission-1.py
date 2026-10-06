import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap) > 1:
            first = -(heapq.heappop(maxheap))
            second = -(heapq.heappop(maxheap))
            diff = first - second
            if diff:
                heapq.heappush(maxheap, -diff)
        if len(maxheap) == 2:
            first = -(heapq.heappop(maxheap))
            second = -(heapq.heappop(maxheap))
            diff = first - second
            return diff
        elif len(maxheap) == 1:
            return -maxheap[0]
        return 0
        