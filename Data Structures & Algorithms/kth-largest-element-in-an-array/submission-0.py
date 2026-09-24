import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # two heaps: max heap and min heap.
        # set the length of min heap to k
        # if larger elem comes into the stream, then we pop the min heap and append curr elem
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]
            

        