class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, path, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(path.copy())
                return
            if idx == len(nums):
                return 
            
            path.append(nums[idx])
            backtrack(idx, path, curr_sum + nums[idx])
            path.pop()
            backtrack(idx+1, path, curr_sum)
            
        backtrack(0, [], 0)
        return res
            

                