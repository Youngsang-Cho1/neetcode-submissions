class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_jump = 0
        i = 0
        while i < len(nums) - 1:
            end = min(i + nums[i], len(nums) - 1)
            if end == len(nums) - 1:
                return curr_jump + 1

            jump_range = nums[i]
            max_jump = -1
            for j in range(i+1, i + jump_range + 1):
                if nums[j] + j > max_jump:
                    max_jump = nums[j] + j
                    i = j
            curr_jump += 1
        return curr_jump
            


            




        