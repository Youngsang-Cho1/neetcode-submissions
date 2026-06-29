class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        counter = 0
        for i in nums:
            if counter == 0:
                majority = i
            if i == majority:
                counter += 1
            else:
                counter -= 1
        return majority

            


        