class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        import copy
    
        seen = set()
        def backtrack(idx, path): # idx += 1. path: include or not
            if idx == len(nums):
                seen.add(tuple(path))
                return
                
            curr = path.copy()
            curr.append(nums[idx])
            backtrack(idx+1, curr)
            curr.pop()
            backtrack(idx+1, curr)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in seen]
                

