class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while left < right and right < len(nums):
            print(nums[left], nums[right])
            if nums[left] == nums[right]:
                del nums[right]
            else:
                right += 1
                left += 1
        return len(nums)

