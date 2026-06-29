class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        store = [0] * len(nums)
        for idx, i in enumerate(nums):
            store[(idx + k) % len(nums)] = i
        nums[:] = store
        

        

            
        