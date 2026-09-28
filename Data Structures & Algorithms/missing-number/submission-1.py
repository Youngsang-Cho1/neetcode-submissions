class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(range(0, len(nums) + 1))
        for num in nums:
            total -= num
        return total
        