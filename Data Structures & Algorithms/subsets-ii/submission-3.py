class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        seen = set()
        def backtrack(idx, path): # idx += 1. path: include or not
            if idx == len(nums):
                seen.add(tuple(path))
                return
                
            path.append(nums[idx])
            backtrack(idx+1, path)
            path.pop()
            backtrack(idx+1, path)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in seen]
                

