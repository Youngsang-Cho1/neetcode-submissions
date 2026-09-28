class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = 1000
        while l <= r:
            mid = (l + r) // 2
            min_val = min(nums[mid], min_val)
            if nums[l] > nums[r]: # rotated
                if nums[mid] < nums[r]: 
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] > nums[l]: # sorted
                r = mid - 1
            else:
                return min_val
        return min_val
            


        