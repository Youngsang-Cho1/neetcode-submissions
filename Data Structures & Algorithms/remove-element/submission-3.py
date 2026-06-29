class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while val in nums:
            if nums[idx] == val:
                nums.remove(val)
            else:
                idx +=1
            
        return len(nums)


        