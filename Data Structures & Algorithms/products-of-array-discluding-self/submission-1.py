class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        curr = 1
        for i in range(len(nums)):
            prefix[i] = curr
            curr *= nums[i]
        #print(prefix)

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = curr
            curr *= nums[i]
        #print(suffix)

        return [p * s for p,s in zip(prefix, suffix)]


                



            

        