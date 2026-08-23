import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxheap = [-i for i in nums]
        self.k = k
        heapq.heapify(self.maxheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxheap, -val)
        print(self.maxheap)
        store = []
        for i in range(self.k-1):
            curr = heapq.heappop(self.maxheap)
            print(curr)
            store.append(curr)
        res = -(self.maxheap[0])
        for i in store:
            heapq.heappush(self.maxheap, i)
        return res
        

        
