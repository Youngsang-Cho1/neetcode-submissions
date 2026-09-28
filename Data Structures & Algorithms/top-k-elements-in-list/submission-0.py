from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        max_heap = []
        res = []
        for key, val in c.items():
            heapq.heappush(max_heap, (-val, key))
        for _ in range(k):
            max_val, key = heapq.heappop(max_heap)
            res.append(key)
        return res
            




        