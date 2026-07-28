class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def backtrack(idx, total):
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
        return res

            

              

        
        