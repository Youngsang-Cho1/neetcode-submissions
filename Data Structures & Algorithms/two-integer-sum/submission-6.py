from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in d:
                return [d[diff], idx]
            else:
                d[i] = idx 