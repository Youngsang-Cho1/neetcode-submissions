class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        num_dict = {}
        for i in nums:
            if i in num_dict.keys():
                num_dict[i] += 1
            else:
                num_dict[i] = 1
                
            if num_dict[i] >= majority:
                return i
            

            


        