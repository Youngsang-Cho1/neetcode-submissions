class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0 : 1}
        prev = 0
        res = 0
        for i in nums:
            curr = prev + i
            diff = curr - k
            if diff in prefix_sum.keys():
                res += prefix_sum[diff]
            if curr in prefix_sum.keys():
                prefix_sum[curr] += 1
            else:
                prefix_sum[curr] = 1
            prev = curr
        return res


        

            