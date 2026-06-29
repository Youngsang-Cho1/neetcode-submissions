class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        l = self.sortArray(nums[0:mid]) 
        r = self.sortArray(nums[mid:]) 

        res = []
        i,j = 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        
        while i < len(l):
            res.append(l[i])
            i += 1

        while j < len(r):
            res.append(r[j])
            j += 1

        return res

        


            