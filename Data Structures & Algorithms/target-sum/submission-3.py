class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = {}
        def dp(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0

            if (idx, total) in memo:
                return memo[(idx, total)]

            memo[(idx, total)] = (
                dp(idx + 1, total + nums[idx])
                + dp(idx + 1, total - nums[idx])
            )

            return memo[(idx, total)]
        return dp(0, 0)
        '''def backtrack(idx, total):
            nonlocal res
            if idx == len(nums) - 1:
                curr = nums[idx]
                if total + curr == target:
                    res += 1
                if total - curr == target:
                    res += 1
                return
            curr = nums[idx]
            backtrack(idx + 1, total + curr)
            backtrack(idx + 1, total - curr)
        backtrack(0,0)
        return res'''

            

              

        
        