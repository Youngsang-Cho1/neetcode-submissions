from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque()
        c = Counter(tasks)

        usable = [-val for val in c.values()]
        heapq.heapify(usable)
        time = 0

        while usable or cooldown:
            time += 1

            if usable:
                curr = -heapq.heappop(usable)
                if curr > 1:
                    cooldown.append((-(curr - 1), time + n))
            if cooldown and cooldown[0][1] <= time:
                available = cooldown.popleft()
                heapq.heappush(usable, available[0])
        return time






