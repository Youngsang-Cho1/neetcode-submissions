class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        d = defaultdict(set)

        for x,y in edges:
            d[x].add(y)
            d[y].add(x)
        
        visited = set()
        res = 0

        for i in range(0, n):
            if i not in visited:
                q = deque()
                q.append(i)
                while q:
                    curr = q.popleft()
                    visited.add(curr)
                    for neighbor in d[curr]:
                        if neighbor not in visited:
                            q.append(neighbor)
                res += 1
        return res
            
            


        