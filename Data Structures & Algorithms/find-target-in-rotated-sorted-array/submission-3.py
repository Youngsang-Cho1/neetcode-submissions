class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search: mid > r -> rotation
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > nums[r]: # r side rotated, l side sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else: # l side rotated, r side sorted
                if nums[r] >= target > nums[mid]: 
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
            
            

        ''' 
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid

            elif nums[l] <= nums[mid]:  
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else: 
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
           
        return -1
'''

        