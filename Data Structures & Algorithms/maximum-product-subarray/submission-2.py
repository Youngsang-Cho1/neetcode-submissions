class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = nums[0]
        minn = nums[0]
        res = maxx
        for i in range(1, len(nums)):
            curr = nums[i]
            maxx, minn = max(curr, maxx * curr, minn * curr), min(curr, maxx * curr, minn * curr)
            res = max(res, maxx)
            
        return res