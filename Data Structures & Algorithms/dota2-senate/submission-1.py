from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_r = deque()
        queue_d = deque()

        for idx, i in enumerate(senate):
            if i == "R":
                queue_r.append(idx)
            elif i == "D":
                queue_d.append(idx)
        print(queue_r, queue_d)

        while queue_r and queue_d:
            R = queue_r.popleft()
            D = queue_d.popleft()
            if R < D: # if R's idx is first compared to that of D's
                queue_r.append(R + len(senate)) # Re-insert R to the queue while still popping D
            else:
                queue_d.append(D + len(senate))
            print(queue_r, queue_d)
        return "Radiant" if queue_r else "Dire"

        
        
        
        