class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(0, len(nums)):
            print(num_dict)
            difference = target - nums[i]
            if difference in num_dict.keys():
                return [num_dict[difference], i]
            else:
                num_dict[nums[i]] = i
                
            
                

        