class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l != len(numbers) - 1:
            for r in range(1, len(numbers)):
                two_sum = numbers[l] + numbers[r]
                if two_sum == target:
                    return [l+1, r+1]
            l += 1