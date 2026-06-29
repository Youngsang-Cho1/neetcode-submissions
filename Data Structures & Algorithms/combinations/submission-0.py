class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(idx, nums): # idx -> current value    nums -> combination
            # print(nums)
            if len(nums) == k:
                if nums not in res:
                    res.append(nums.copy())
                return
            if idx > n:
                return
            # path 1: including
            nums.append(idx)
            backtrack(idx + 1, nums)
            nums.pop()

            # path2: not including
            backtrack(idx + 1, nums)
        backtrack(1, [])
        return res
            
            
        