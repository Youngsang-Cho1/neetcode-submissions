class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(curr, target, visited):
            if curr == target:
                return True
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False


        for u, v in edges:
            if u in graph and v in graph:
                if dfs(u,v,set()):
                    return [u,v]
            graph[u].append(v)
            graph[v].append(u)
        
             

        
            
            

            
        