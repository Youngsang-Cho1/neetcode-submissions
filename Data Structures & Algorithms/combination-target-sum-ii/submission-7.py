class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        visited = []
        candidates.sort()
        def backtrack(idx, total, path):
            if total == target and path not in visited:
                visited.append(path.copy()) 
                return
            if idx == len(candidates):
                return
            if total > target:
                return

            curr = candidates[idx]
            path.append(curr)
            backtrack(idx + 1, total + curr, path)
            path.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx + 1, total, path)
        backtrack(0, 0, [])
        res = []

        return visited


