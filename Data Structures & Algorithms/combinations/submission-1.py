class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, nums): # idx -> current value    nums -> combination
            # print(nums)
            if len(nums) == k:
                if nums not in res:
                    res.append(nums.copy())
                return
            for curr in range(start, n + 1):
                nums.append(curr)
                backtrack(curr + 1, nums)
                nums.pop()
        backtrack(1, [])
        return res
            
            
        