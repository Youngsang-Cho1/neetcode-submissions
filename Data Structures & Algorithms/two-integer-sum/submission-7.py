from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for idx, i in enumerate(nums):
            d[i] = idx
        for idx, i in enumerate(nums):
            curr = target - i
            if curr in d:
                if d[curr] != idx:
                    return sorted([d[curr], idx])
            
            
        