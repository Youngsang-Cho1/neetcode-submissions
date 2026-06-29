class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_dict = {}
        for i in nums:
            if i not in color_dict.keys():
                color_dict[i] = 1
            else:
                color_dict[i] += 1
        
        idx = 0
        red_count = color_dict[0] if 0 in color_dict.keys() else 0
        white_count = color_dict[1] if 1 in color_dict.keys() else 0
        blue_count = color_dict[2] if 2 in color_dict.keys() else 0

        for i in range (red_count):
            nums[idx] = 0
            idx += 1
        for i in range (white_count):
            nums[idx] = 1
            idx += 1
        for i in range (blue_count):
            nums[idx] = 2
            idx += 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        