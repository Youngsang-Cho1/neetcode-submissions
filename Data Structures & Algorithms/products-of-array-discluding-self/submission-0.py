class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix_product = 1
        suffix = []
        suffix_product = 1
        answer = []
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix_product)
            prefix_product *= nums[i]
        print(prefix)
        
        for i in range(len(nums), 0, -1):
            if i == len(nums):
                suffix.append(1)
            else:
                suffix.append(suffix_product)
            suffix_product *= nums[i - 1]
        print(suffix)

        for i in range(0, len(nums)):
            answer.append(prefix[i]*suffix[len(nums) -1 -i])
        return answer


                



            

        