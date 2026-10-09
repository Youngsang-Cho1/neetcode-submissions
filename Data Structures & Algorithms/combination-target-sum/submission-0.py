class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        visited = set()
        def backtrack(idx, path):
            curr_sum = sum(path)
            if curr_sum > target:
                return
            if curr_sum == target and tuple(path) not in visited:
                visited.add(tuple(path))
            if idx == len(nums):
                return 
            
            path.append(nums[idx])
            backtrack(idx, path)
            path.pop()
            backtrack(idx+1, path)
            
        backtrack(0, [])
        return [list(elem) for elem in visited]
            

                