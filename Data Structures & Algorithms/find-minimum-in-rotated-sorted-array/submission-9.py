class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]: # rotated - min in right half
                l = mid + 1
            else: # sorted - min in left half
                r = mid
        return nums[l]


