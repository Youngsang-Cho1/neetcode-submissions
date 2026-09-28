class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph: graph[curr] = prereq form
        # dfs to traverse all the way to the end of the prereq
        # use visiting, visited to follow.
        # add each course to visiting/visited.
        # if cycle, return False
        # if visited > numCourses then return false.

        res = []
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def is_acyclic(curr, visiting, visited):
            if curr in visiting:
                return False
            if curr in visited:
                return True

            visiting.add(curr)

            for prereq in graph[curr]:
                next_c = is_acyclic(prereq, visiting, visited)
                if not next_c:
                    return False
            res.append(curr)
            visiting.remove(curr)
            visited.add(curr)
            return True
        
        visiting, visited = set(), set()
        for course in range(numCourses):
            if course not in visited:
                check = is_acyclic(course, visiting, visited) 
                if check == False:
                    return []

        return res



        

        