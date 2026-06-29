class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        int_dict = {}
        for i in nums:
            if i not in int_dict:
                int_dict[i] = 1
            else:
                return i


        