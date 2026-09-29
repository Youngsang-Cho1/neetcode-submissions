class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res = []
        for l in range(len(nums)-2):
            r = l + 1
            while r < len(nums):
                d[nums[l]] -= 1
                d[nums[r]] -= 1
                target = -(nums[l] + nums[r])
                if target in d and d[target] > 0:
                    if sorted((nums[l], nums[r], target)) not in res:
                        res.append(sorted((nums[l], nums[r], target)))
                d[nums[l]] += 1
                d[nums[r]] += 1
                r += 1
        return res
