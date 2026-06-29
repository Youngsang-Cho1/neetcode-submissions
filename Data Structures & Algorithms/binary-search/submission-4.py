class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while ((left <= right)):
            curr_idx = (left + right) // 2
            if target == nums[curr_idx]:
                return curr_idx
            elif target < nums[curr_idx]:
                right = curr_idx - 1
            else: # target > nums[curr_idx]
                left = curr_idx + 1
        return -1



        