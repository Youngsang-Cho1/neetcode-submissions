class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        goal = sum(nums) // 2
        def dfs(i, total):
            if i == len(nums):
                return total == goal
            
            include = dfs(i+1, total + nums[i])
            not_include = dfs(i+1, total)

            return include or not_include

        return dfs(0, 0)

            
                
            
        
        