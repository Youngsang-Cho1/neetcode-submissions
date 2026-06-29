class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = []
        
        nums_set = sorted(set(nums))
        print(nums_set)
        prev = nums[0]
        counter = 1

        for i in nums_set:
            print(prev, i)
            if i == prev + 1:
                counter += 1
            else:
                res.append(counter)
                counter = 1
            prev = i

        res.append(counter)
        res.sort(reverse = True)
        return res[0]


        