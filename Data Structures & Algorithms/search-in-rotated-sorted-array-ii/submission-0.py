class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        temp = set(nums)
        for i in temp:
            if i == target:
                return True
        return False

        