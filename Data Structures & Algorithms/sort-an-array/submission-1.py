class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        elif len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            self.sortArray(left)
            self.sortArray(right)
            
            i = j = idx = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[idx] = left[i]
                    i += 1
                else:
                    nums[idx] = right[j]
                    j += 1
                idx += 1

            while i < len(left):
                nums[idx] = left[i]
                idx += 1
                i += 1

            while j < len(right):
                nums[idx] = right[j]
                idx += 1
                j += 1

            return (nums)
            




