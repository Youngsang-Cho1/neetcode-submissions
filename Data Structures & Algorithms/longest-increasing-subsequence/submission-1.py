class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)): # curr elem
            for j in range(i): # prev elems
                if nums[j] < nums[i]:
                    # update dp
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        # 0 1 0 2 3

        