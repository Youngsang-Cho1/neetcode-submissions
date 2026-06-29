class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums)//3
        hashmap = {}
        res = []
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        for key, val in hashmap.items():
            if val > threshold:
                res.append(key)
        return res



        