class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        if len(nums) <= 3:
            return max(nums)
        dp1 = nums[:-1]
        dp1[1] = max(dp1[0], dp1[1])
        dp2 = nums[1:]
        dp2[1] = max(dp2[0], dp2[1])
        for i in range(2,len(dp1)):
            dp1[i] = max(dp1[i-2] + dp1[i], dp1[i-1])
        print(dp1)

        for i in range(2, len(dp2)):
            dp2[i] = max(dp2[i-2] + dp2[i], dp2[i-1])
        print(dp2)
        return max(dp1[-1], dp2[-1])



        

            
        