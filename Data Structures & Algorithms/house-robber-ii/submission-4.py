class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        dp_first = [0 for _ in range(len(nums))]
        dp_first[0] = nums[0]
        dp_first[1] = nums[0] if nums[0] > nums[1] else nums[1]
        dp_last = [0 for _ in range(len(nums))]
        dp_last[1] = nums[1]
        dp_last[2] = nums[1] if nums[1] > nums[2] else nums[2]

        for i in range(2, len(dp_first)):
            dp_first[i] = max(dp_first[i-1], dp_first[i-2] + nums[i])
        
        for j in range(3, len(dp_last)):
            dp_last[j] = max(dp_last[j-1], dp_last[j-2] + nums[j])
            print(dp_last)

        return(max(dp_first[-2], dp_last[-1]))
            
        