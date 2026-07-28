from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq_d = defaultdict(list)
        res = []
        for prereq, curr in prerequisites:
            prereq_d[curr].append(prereq)

        for query in queries:
            u, v = query
            is_prereq = False
            visited = set()
            q = deque([v]) 
            while q:
                curr = q.popleft()
                if curr == u:
                    is_prereq = True
                    break

                for prereq in prereq_d[curr]:
                    if prereq not in visited:
                        visited.add(prereq)
                        q.append(prereq)
            res.append(is_prereq)
        return res
        
