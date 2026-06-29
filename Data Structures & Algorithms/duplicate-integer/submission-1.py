class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}
        for num in nums: 
            if num not in dup_dict.keys():
                dup_dict[num] = 1
            else:
                return True
        return False

        