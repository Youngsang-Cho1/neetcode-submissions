class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict

        d = defaultdict(set)
        for start, end in edges:
            d[start].add(end)
            d[end].add(start)

        def dfs(node, visiting, visited):
            #print(node, visiting, visited)
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)

            for neighbor in d[node]:
                nextt = dfs(neighbor, visiting, visited)
                if nextt == False:
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        visiting, visited = set(), set()
        if not edges:
            return True

        return dfs(edges[0][0], visiting, visited) and len(visited) == n
            




        