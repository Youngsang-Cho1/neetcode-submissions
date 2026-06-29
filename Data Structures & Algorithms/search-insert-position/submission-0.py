class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            curr_idx = (right + left) // 2
            if nums[curr_idx] == target:
                return curr_idx
            elif target > nums[curr_idx]:
                left = curr_idx + 1
            else:
                right = curr_idx - 1
        return (left)

        