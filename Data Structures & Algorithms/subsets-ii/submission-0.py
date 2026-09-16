class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        import copy
        nums.sort()
        res = []
        seen = set()
        def backtrack(idx, path): # idx += 1. path: include or not
            if idx == len(nums):
                
                if tuple(path) not in seen:
                    res.append(path.copy())
                    seen.add(tuple(path))
                return
            else:
                curr = path.copy()
                curr.append(nums[idx])
                backtrack(idx+1, curr)
                curr.pop()
                backtrack(idx+1, curr)
        backtrack(0, [])
        return res
                

