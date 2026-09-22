class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # dfs
        graph = defaultdict(list)
        for i in prerequisites:
            course, prereq = i
            graph[course].append(prereq)
        
        #print(graph)
        visiting, visited = set(), set()
        def dfs(curr, visiting, visited):
            if curr in visiting:
                return False
            if curr in visited:
                return True
            
            visiting.add(curr)
            for p in graph[curr]:
                nextt = dfs(p, visiting, visited)
                if not nextt:
                    return False
            visiting.remove(curr)
            visited.add(curr)
            return True
        
        for key in list(graph.keys()):
            if key not in visited:
                curr = dfs(key, visiting, visited)
                if curr == False:
                    return False
        return True


